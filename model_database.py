import json
import os

class ModelDatabase:
    def __init__(self, data_file='models.json'):
        self.data_file = data_file
        self.models = self.load_data()  # Load existing data on init

    def load_data(self):
        """Load models from JSON file if it exists."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def save_data(self):
        """Save models to JSON file."""
        with open(self.data_file, 'w') as f:
            json.dump(self.models, f, indent=4)
        print(f"💾 Data saved to {self.data_file}")

    def add_model(self, name, pricing, dos, donts, profile):
        """
        Add a new model to the database.
        - dos and donts are lists of strings (Yes/No items).
        - pricing and profile can be multi-line strings.
        """
        self.models[name] = {
            'pricing': pricing,
            'dos': dos if isinstance(dos, list) else [dos],
            'donts': donts if isinstance(donts, list) else [donts],
            'profile': profile
        }
        self.save_data()
        print(f"✅ Added/Updated model: {name}")

    def remove_model(self, name):
        """Remove a model by name."""
        if name in self.models:
            del self.models[name]
            self.save_data()
            print(f"🗑️ Removed model: {name}")
        else:
            print(f"❌ Model '{name}' not found.")

    def view_model(self, name):
        """View full details of a model."""
        if name in self.models:
            model = self.models[name]
            print(f"\n📋 Model: **{name}**")
            print(f"💰 Pricing:\n{model['pricing']}")
            print(f"✅ Do's: {', '.join(model['dos'])}")
            print(f"❌ Don'ts: {', '.join(model['donts'])}")
            print(f"📝 Profile:\n{model['profile']}\n")
        else:
            print(f"❌ Model '{name}' not found.")

    def list_models(self):
        """List all models in the database."""
        if not self.models:
            print("📂 No models in database yet. Add one to get started!")
        else:
            print("\n📂 Available Models:")
            for name in sorted(self.models.keys()):
                print(f"  - {name}")
            print()

    def interactive_mode(self):
        """Simple command-line interface for interaction."""
        print("🤖 Welcome to the Model Database!")
        print("Commands: add, remove, view, list, quit")
        
        while True:
            cmd = input("\n> ").strip().lower()
            if cmd == 'quit':
                self.save_data()  # Auto-save on exit
                print("👋 Goodbye!")
                break
            elif cmd == 'list':
                self.list_models()
            elif cmd == 'add':
                name = input("Model name: ")
                print("Pricing (multi-line; end with empty line):")
                pricing_lines = []
                while True:
                    line = input()
                    if not line:
                        break
                    pricing_lines.append(line)
                pricing = '\n'.join(pricing_lines)
                
                print("Do's (comma-separated Yes/No items): ")
                dos_input = input()
                dos = [d.strip() for d in dos_input.split(',') if d.strip()]
                
                print("Don'ts (comma-separated No items): ")
                donts_input = input()
                donts = [d.strip() for d in donts_input.split(',') if d.strip()]
                
                print("Profile (multi-line; end with empty line):")
                profile_lines = []
                while True:
                    line = input()
                    if not line:
                        break
                    profile_lines.append(line)
                profile = '\n'.join(profile_lines)
                
                self.add_model(name, pricing, dos, donts, profile)
            elif cmd == 'remove':
                name = input("Model name to remove: ")
                self.remove_model(name)
            elif cmd == 'view':
                name = input("Model name to view: ")
                self.view_model(name)
            else:
                print("Unknown command. Try 'add', 'remove', 'view', 'list', or 'quit'.")

# Starter data: Load Roxie Sinner and examples
if __name__ == "__main__":
    db = ModelDatabase()
    
    # Add Roxie Sinner (your example data)
    if 'ROXIE SINNER' not in db.models:
        db.add_model(
            "ROXIE SINNER",
            """PRICE LIST - LAST UPDATED: 08/12/2024
Client: Roxie Sinner
Summary:
1. Video calls via OF 1-1 live 
2. no Arab name calling
3. No hijab scenes
4.No religious related sexting or content 
5. CUSTOMS TURNAROUND: Try to do them in 4-5 days
7. can do masturbation during video calls
8. Agency to book her for pro-porn shooting 9 . CAN DO BG CONTENT but NO LOWER THAN 600 
09. CAN FOLLOW \\ ADD FAN BACK ( IG )
BUT WILL NEVER MESSAGE. PRICE STARTS AT 40+
When closing VC please note 2 mins is the minimum. 

Fully clothed boob/booty pics	$5+
Booty pics in panties/boob pics in bra	$5+
Dick rating text	$5+
Naked boob/ass pictures	$7+
Pussy pictures	$10+
Dick rating speech with persons name	$15+
Topless dick rating	$40+
Masturbation videos	$15+
B/G Blowjob Videos	$25+
Sex Scenes 	$30+
Signed Polaroid	$50+
Custom Pictures (Clothing & No Face)	$10+
Custom Pictures (Clothing & Face)	$15+
Custom Pictures (Naked & No Face)	$25+
Custom Pictures (Naked & Face)	$30+
"Custom videos (fully clothed/lingerie)
2 minutes minimum duration"	$15 per min
"Custom videos (Naked)
2 minutes minimum duration "	$100 per min
VIDEO CALLS ( 3mins minimum) 	$50 per min (maybe well lower it if needed)
Joi videos	$30+
Used Panties 	$100+
Used Lingerie	$150+
THESE ARE MINIMUM PRICES FEEL FREE TO CHARGE MORE IF YOU CAN, BUT DON'T GO BELOW THESE UNLESS APPROVED BY MANAGEMENT!""",
            [
                "Fully Nude: TRUE",
                "Shows Face in Explicit Content: TRUE",
                "Dirty Talk in Videos: TRUE",
                "Finger sucking: TRUE",
                "Signed Polaroids: TRUE",
                "Video Calls: TRUE",
                "Text Dick Rates: TRUE",
                "Voice Dick Rates: TRUE",
                "Video Dick Rates with face: TRUE",
                "Small Penis Humiliation: TRUE",
                "Femdom Voice notes: TRUE",
                "Strapon Content: TRUE",
                "Non-explicit videos with Face: TRUE",
                "Explicit videos with Face: TRUE",
                "JOI (jerk off instructions) Audio: TRUE",
                "JOI (jerk off instructions) Video: TRUE",
                "Custom Videos: TRUE",
                "Custom Videos Longer than 5 mins: TRUE",
                "Girl/Girl Content: TRUE",
                "Boy/Girl Content: TRUE",
                "Blow Job Content: TRUE",
                "Selling Underwear/Lingerie: TRUE",
                "Dildo Sucking Videos: TRUE",
                "Dildo Masturbation Videos: TRUE",
                "Pussy Pictures: TRUE",
                "Squirting Content: TRUE",
                "Fingering Pussy Videos: TRUE",
                "Naked Ass Pictures: TRUE",
                "Naked Shower Videos: TRUE",
                "Twerking Videos: TRUE",
                "Deepthroat content: TRUE",
                "Fetish self spanking: TRUE"
            ],
            [
                "Femdom Videos: FALSE",
                "Anal masturbation: FALSE",
                "Anal sex video: FALSE",
                "Nipple pinching content: FALSE",
                "Fetish blindfold and self binding: FALSE"
            ],
            """🔹 Model Name: Roxie Sinner
🔹 Important Info: "1. Video calls (SnapChat) - Please ask your TL for the link
2. no Arab name calling
3. No hijab scenes
4.No religious related sexting or content 
5. CUSTOMS TURNAROUND: Try to do them in 4-5 days
6. .
7. can do masturbation during video calls
8. Agency to book her for pro-porn shooting
9. CAN DO BG custom but no lower than 600 
10. DO NOT MENTION ANYTHING RELATED TO ESCORTS OR IRL BOOKINGS
11. CAN FOLLOW \\ ADD FAN BACK ( IG , SNAP)
BUT WILL NEVER MESSAGE. PRICE STARTS AT 40+
12. CANT DO ANAL - EVEN BUTT PLUg
13. Roxie has 6 tattoos
14. No Horse Dildo
15. When closing VC please note 2 mins is the minimum. 
16.  If anyone asks if she’s Muslim, don’t answer with “I’m Syrian”, they’re asking about her religion, not her nationality. Instead, say she’s not Muslim and does not participate in any religion.
17- if fans want to speak in arabic, say english please and explain she doesn't have an arabic keyboard and left syria when she was young so english is easier "
🔸 Texting Style: 
🔸 Chatting Guidelines: 
🌟 VIP Page/GF Exp: "VIP Club: 
Girlfriend Experience: "
👥 Regular Customers: 
🎂 Age: 24 years old | 20/12/2000 
📏 Height: 5”7
🌍 Ethnicity: Arabic
🏡 Hometown: Syria
📍 Location: Las Vegas , USA
🕒 Last Updated: July 1, 2024
💼 Profession: "I shoot pro porn & I take private bookings with fans.
Photography career possible as well & the fans know I shoot film photography "
🎭 Model Niche: No niche just the Arab gf you've always wished for🤣
😄 Personality: "Calls fans - Babe, boo, bby, baby

To laugh - Lmfao, lol or 🤣🤣"
🐾 Pets: "Animal:  2 cats
Breed: N/A
Names: Smoke and Leo

Additional information: Smoke: Smokey colored w white stripes about 12pounds adopted in 2020 sleeps by the TV.
Leo: mini tiger about 14 pounds adopted also in 2020 about 4 months after smoke & he sleeps in my arms w his back holding up my face as a pillow lol"
🧸 Hobbies: Smoking, making jewelry, photography & picnics/nature activities 
💬 Languages Spoken: English  and Arabic
📺 Favourite Media: "🎵 Music:  Rap/hip hop, old 60's & 70's music, r&b, Arabic music & indie

📺 TV/Film: Barely watch tv😭 but if I do it's something comedy, horror or action "
🧍 Body Sizes: "👠 Shoe Size: 9

👙 Bra Size: 34 DD

Waist: 41 inches"
🧷 Body Modifications: All natural
📲 Socials: "https://www.theroxiesinner.com/

https://www.instagram.com/_roxiesinner_/?hl=en

https://www.instagram.com/roxiesinneragain/"
❤️ Relationship Status: 👱🏻‍♀️ Single  
📌 General Info: Friendly, cute, nice, dirty
🎲 Misc Facts: "I'm very friendly & nice to fans both online & in person when I meet them at conventions! So pls translate that well into text!
Also fans know I'm pro Palestine & sometimes they'll text about it or praise me for it & shit just so yk"
"""
        )
    
    # Optional: Add previous AI examples if desired
    # if 'Grok 3' not in db.models:
    #     db.add_model("Grok 3", "Free with limits", ["Use for queries"], ["Exceed quotas"], "xAI model.")
    
    db.interactive_mode()
