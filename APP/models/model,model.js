module.exports = mongoose => {
  var schema = mongoose.Schema(
    {
      id: { type: String, required: true, unique: true },
      name: { type: String, required: true },
      age: { type: Number },
      location: { type: String },
      profile: { type: String, required: true },
      pricing: { type: String, required: true },
      dosAndDonts: { type: String, required: true },
      extraTabs: { type: Array, default: [] },
      history: { type: Array, default: [] }
    },
    { timestamps: true }
  );

  schema.pre('save', function(next) {
    if (this.isModified() && !this.isNew) {
      this.history.push({
        timestamp: new Date(),
        action: 'update',
        changes: this.modifiedPaths()
      });
    }
    next();
  });

  return mongoose.model("Model", schema);
};