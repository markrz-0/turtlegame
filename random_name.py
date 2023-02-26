import random

names = [
    "4-Wheel",
    "Ace",
    "Admiral",
    "Amazon",
    "Amethyst",
    "Ami",
    "Amiga",
    "Amigo",
    "Amor",
    "Amorcita",
    "Amore",
    "Amour",
    "Angel",
    "Anvil",
    "Apple",
    "Apple Jack",
    "Ash",
    "Autumn",
    "Azkaban",
    "Babe",
    "Babs",
    "Baby",
    "Baby Bird",
    "Baby Boo",
    "Baby Cakes",
    "Baby Carrot",
    "Baby Maker",
    "Backbone",
    "Bacon",
    "Baldie",
    "Bambi",
    "Bambino",
    "Bandit",
    "Barbie",
    "Bean",
    "Beanpole",
    "Beast",
    "Beautiful",
    "Beauty",
    "Bebe",
    "Beef",
    "Beetle",
    "Belch",
    "Bellbottoms",
    "Belle",
    "Bello",
    "Bessie",
    "Betty Boop",
    "Biffle",
    "Big Bird",
    "Big Guy",
    "Big Mac",
    "Big Nasty",
    "Birdy",
    "Biscuit",
    "Blimpie",
    "Blondie",
    "Boo",
    "Boo Bear",
    "Boo Boo",
    "Boo Bug",
    "Boomer",
    "Boomhauer",
    "Bootsie",
    "Bossy",
    "Braniac",
    "Braveheart",
    "Bridge",
    "Brown Sugar",
    "Bruiser",
    "Brutus",
    "Bub",
    "Bubba",
    "Bubble Butt",
    "Bubblegum",
    "Bubbles",
    "Buck",
    "Buckeye",
    "Bud",
    "Buddy",
    "Buds",
    "Buffalo",
    "Bug",
    "Bumblebee",
    "Bumpkin",
    "Bunny",
    "Bunny Rabbit",
    "Buster",
    "Butter",
    "Butterbuns",
    "Buttercup",
    "Butterfinger",
    "Butternut",
    "Button",
    "Buzz",
    "C-Dawg",
    "Candy",
    "Candycane",
    "Cannoli",
    "Captain",
    "Captain Crunch",
    "Carrot",
    "Cat",
    "Catwoman",
    "Cello",
    "Chain",
    "Champ",
    "Chance",
    "Cheddar",
    "Cheeky",
    "Cheerio",
    "Cheese",
    "Cheesestick",
    "Cheeto",
    "Chef",
    "Cherry",
    "Chewbacca",
    "Chica",
    "Chicken Legs",
    "Chicken Wing",
    "Chickie",
    "Chico",
    "Chief",
    "Chili",
    "Chip",
    "Chiquita",
    "Chubs",
    "Chuckles",
    "Chum",
    "Chump",
    "Cindy Lou Who",
    "Cinnamon",
    "Cloud",
    "Coach",
    "Coke Zero",
    "Cold Brew",
    "Cold Front",
    "Colonel",
    "Con",
    "Conductor",
    "Cookie",
    "Cookie Dough",
    "Cotton",
    "Cottonball",
    "Cowboy",
    "Creedence",
    "Creep",
    "Cricket",
    "Cruella",
    "Crumbles",
    "Cuddle Pig",
    "Cuddles",
    "Cumulus",
    "Cupcake",
    "Cutie",
    "Cutie Pie",
    "Daffodil",
    "Daria",
    "Darling",
    "Dear",
    "Dearest",
    "Dearey",
    "Diesel",
    "Diet Coke",
    "Dilly Dally",
    "Dimples",
    "Dimpling",
    "Dingo",
    "Dino",
    "Dinosaur",
    "Dirt",
    "Dirty Harry",
    "DJ",
    "Doc",
    "Doctor",
    "Doll",
    "Dolly",
    "Donut",
    "Donuts",
    "Doobie",
    "Doofus",
    "Dorito",
    "Dork",
    "Dot",
    "Dots",
    "Dottie",
    "Double Bubble",
    "Double Double",
    "Dracula",
    "Dragon",
    "Dragonfly",
    "Drake",
    "Dreamey",
    "Dropout",
    "Duckling",
    "Ducky",
    "Dud",
    "Dulce",
    "Dum Dum",
    "Dumbledore",
    "Dummy",
    "Dunce",
    "Eagle",
    "Einstein",
    "Elf",
    "Fatty",
    "Fattykins",
    "Fellow",
    "Fido",
    "Fiesta",
    "Fifi",
    "Figgy",
    "Filly Fally",
    "First Mate",
    "Flower",
    "Fly",
    "Flyby",
    "Focker",
    "Fox",
    "Foxy",
    "Foxy Lady",
    "Foxy Mama",
    "Frankfurter",
    "Frau Frau",
    "Frauline",
    "Freak",
    "Freckles",
    "French Fry",
    "Friendo",
    "Frodo",
    "Frogger",
    "Fun Dip",
    "Fun Size",
    "Fury",
    "Gams",
    "Gator",
    "General",
    "Genius",
    "Ghoulie",
    "Giggles",
    "Ginger",
    "Gingersnap",
    "Gizmo",
    "Goblin",
    "Golden Graham",
    "Goldilocks",
    "Goon",
    "Goonie",
    "Goose",
    "Gordo",
    "Grease",
    "Green Giant",
    "Grumpy",
    "Guapo",
    "Gumdrop",
    "Gummi Bear",
    "Gummy Pop",
    "Half Pint",
    "Halfling",
    "Halfmast",
    "Hammer",
    "Happy",
    "Harry Potter",
    "Hawk",
    "Headlights",
    "Heisenberg",
    "Hermione",
    "Herp Derp",
    "Highbeam",
    "Homer",
    "Honey Locks",
    "Honey Pie",
    "Honeybun",
    "Hot Pepper",
    "Hot Sauce",
    "Huggie",
    "Hulk",
    "Ice Queen",
    "Inchworm",
    "Itchy",
    "Jackrabbit",
    "Janitor",
    "Jet",
    "Joker",
    "Juicy",
    "Junior",
    "Kid",
    "Kirby",
    "Kit-Kat",
    "Kitten",
    "Kitty",
    "Knucklebutt",
    "Lady",
    "Ladybug",
    "LaLa",
    "Lefty",
    "Lil Girl",
    "Lil Mama",
    "Lion",
    "Little Bear",
    "Lobster",
    "Loosetooth",
    "Loser",
    "Lovely",
    "Lover",
    "Lovey",
    "Lulu",
    "Luna",
    "Mad Max",
    "Maestro",
    "Manatee",
    "Marge",
    "Marshmallow",
    "Master",
    "Matey",
    "Midge",
    "Mimi",
    "Mini Me",
    "Mini Mini",
    "Mini Skirt",
    "Miss Piggy",
    "Mistress",
    "MomBod",
    "Monkey",
    "Moose",
    "Mountain",
    "Mouse",
    "Mr. Clean",
    "Ms. Congeniality",
    "Muffin",
    "Munchkin",
    "Muscles",
    "Music Man",
    "Mustache",
    "Nerd",
    "Numbers",
    "Oompa Loompa",
    "Pansy",
    "Papito",
    "PB&J",
    "Pearl",
    "Pebbles",
    "Pecan",
    "Peep",
    "Peppa Pig",
    "Peppermint",
    "Pickle",
    "Pickles",
    "Pig",
    "Piggy",
    "Piglet",
    "Pinata",
    "Pinkie",
    "Pintsize",
    "Pixie",
    "Pixie Stick",
    "Pookie",
    "Pop Tart",
    "Popeye",
    "Pork Chop",
    "Prego",
    "Pretty Lady",
    "Princess",
    "Psycho",
    "Punk",
    "Pyscho",
    "Queen Bee",
    "Queenie",
    "Rabbit",
    "Rainbow",
    "Raindrop",
    "Raisin",
    "Rambo",
    "Rapunzel",
    "Red",
    "Red Hot",
    "Red Velvet",
    "Redbull",
    "Righty",
    "Ringo",
    "Robin",
    "Rocketfuel",
    "Rockette",
    "Romeo",
    "Rosebud",
    "Rosie",
    "Rubber",
    "Rufio",
    "Rumplestiltskin",
    "Salt",
    "Sassafras",
    "Sassy",
    "Scarlet",
    "Schnookums",
    "Scout",
    "Senior",
    "Senorita",
    "Sherlock",
    "Shnookie",
    "Short Shorts",
    "Shorty",
    "Shrinkwrap",
    "Shuttershy",
    "Silly Sally",
    "Silly Gilly",
    "Skinny Jeans",
    "Skinny Minny",
    "Skipper",
    "Skunk",
    "Sleeping Beauty",
    "Slick",
    "Slim",
    "Smarty",
    "Smiley",
    "Smirk",
    "Smoochie",
    "Smudge",
    "Snake",
    "Snickerdoodle",
    "Snickers",
    "Snoopy",
    "Snow White",
    "Snuggles",
    "Sourdough",
    "Speedy",
    "Spicy",
    "Sport",
    "Spud",
    "Squirt",
    "Starbuck",
    "Stitch",
    "String Bean",
    "Stud",
    "Sugar",
    "Sunny",
    "Sunshine",
    "Superman",
    "Sweety",
    "Sweet Tea",
    "Sweet 'n Sour",
    "Sweetums",
    "Swiss Miss",
    "T-Dawg",
    "Taco",
    "Tank",
    "Tarzan",
    "Tata",
    "Tater",
    "Tater Tot",
    "Teeny",
    "Terminator",
    "Guy",
    "Hulk",
    "Thor",
    "Thumper",
    "Thunder Thighs",
    "Ticklebutt",
    "Tickles",
    "Tiny",
    "Tomcat",
    "Toodles",
    "Toots",
    "Tootsie",
    "Tough Guy",
    "Turkey",
    "Turtle",
    "Twig",
    "Twiggy",
    "Twinkie",
    "Twinkly",
    "Twix",
    "Twizzler",
    "Tyke",
    "Weiner",
    "Weirdo",
    "Wifey",
    "Hubby",
    "Wilma",
    "Winnie"
]

def random_name() -> str:
    return random.choice(names)