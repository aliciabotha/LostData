require("dotenv").config();
const express = require("express");
const cors = require("cors");
const path = require("path");
const session = require("express-session");
const multer = require("multer");
const upload = multer({ dest: 'uploads/' });
const fs = require("fs");
const csvParser = require("csv-parser");
const { Parser } = require("json2csv");

const app = express();

app.use(cors({ origin: "*" }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(session({
  secret: 'secret-key',
  resave: false,
  saveUninitialized: true
}));
app.use(express.static(path.join(__dirname, "public")));

const db = require("./APP/models");
db.mongoose.connect(process.env.MONGODB_URI).then(() => console.log("DB connected")).catch(err => console.log(err));

app.post("/api/login", (req, res) => {
  const { email } = req.body;
  req.session.user = { email, role: email.endsWith('@admin.com') ? 'admin' : 'chatter' };
  res.json({ role: req.session.user.role });
});

app.post("/api/logout", (req, res) => {
  req.session.destroy();
  res.json({ message: 'Logged out' });
});

const isAdmin = (req, res, next) => {
  if (req.session.user && req.session.user.role === 'admin') next();
  else res.status(403).json({ message: 'Admin required' });
};

const Model = db.models;

app.get("/api/models", async (req, res) => {
  try {
    const models = await Model.find({}).sort({ name: 1 });
    res.json(models);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get("/api/models/:id", async (req, res) => {
  try {
    const model = await Model.findById(req.params.id);
    res.json(model);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post("/api/models", isAdmin, async (req, res) => {
  try {
    const model = new Model(req.body);
    model.history.push({ timestamp: new Date(), action: 'create', user: req.session.user.email, changes: 'Initial creation' });
    await model.save();
    res.json(model);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.put("/api/models/:id", isAdmin, async (req, res) => {
  try {
    const model = await Model.findById(req.params.id);
    model.history.push({ timestamp: new Date(), action: 'update', user: req.session.user.email, changes: Object.keys(req.body) });
    Object.assign(model, req.body);
    await model.save();
    res.json(model);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.delete("/api/models/:id", isAdmin, async (req, res) => {
  try {
    await Model.findByIdAndDelete(req.params.id);
    res.json({ message: 'Deleted' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get("/api/export/json", isAdmin, async (req, res) => {
  try {
    const data = await Model.find({});
    res.json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get("/api/export/csv", isAdmin, async (req, res) => {
  try {
    const data = await Model.find({});
    const parser = new Parser();
    const csv = parser.parse(data);
    res.header("Content-Type", "text/csv");
    res.attachment("models.csv");
    res.send(csv);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post("/api/import/csv", isAdmin, upload.single('file'), (req, res) => {
  const results = [];
  fs.createReadStream(req.file.path)
    .pipe(csvParser())
    .on("data", (data) => results.push(data))
    .on("end", () => {
      Model.insertMany(results).then(() => res.json({ message: 'Imported' })).catch(err => res.status(500).json(err));
    });
});

app.get(/^\/(?!api).*/, (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server on ${PORT}`));