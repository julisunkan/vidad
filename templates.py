VIDEO_TEMPLATES = [
    {
        "id": 1,
        "name": "Corporate Introduction",
        "description": "Professional introduction for your business",
        "transitions": ["fadein", "fadeout"],
        "duration": 10,
        "text_slots": [
            {"text": "Welcome to [Business Name]", "position": "center", "start": 1, "duration": 3},
            {"text": "Innovative Solutions for You", "position": "center", "start": 5, "duration": 3}
        ],
        "image_slots": 2,
        "effects": ["disintegrate"],
        "bg_color": (30, 60, 114)
    },
    {
        "id": 2,
        "name": "Product Launch",
        "description": "Exciting announcement for new products",
        "transitions": ["zoom", "slide"],
        "duration": 12,
        "text_slots": [
            {"text": "Introducing [Product Name]", "position": "center", "start": 2, "duration": 4},
            {"text": "Get Yours Today!", "position": "center", "start": 7, "duration": 3}
        ],
        "image_slots": 3,
        "effects": ["reintegrate"],
        "bg_color": (220, 50, 50)
    },
    {
        "id": 3,
        "name": "Testimonial Video",
        "description": "Showcase customer success stories",
        "transitions": ["crossfade"],
        "duration": 15,
        "text_slots": [
            {"text": "What Our Customers Are Saying", "position": "center", "start": 1, "duration": 4},
            {"text": "Real Stories, Real Results", "position": "center", "start": 9, "duration": 4}
        ],
        "image_slots": 2,
        "effects": ["disintegrate", "reintegrate"],
        "bg_color": (70, 130, 180)
    },
    {
        "id": 4,
        "name": "Sale Promotion",
        "description": "Drive urgency with special offers",
        "transitions": ["fadein", "zoom"],
        "duration": 8,
        "text_slots": [
            {"text": "Limited Time Offer!", "position": "center", "start": 1, "duration": 3},
            {"text": "Up to 50% Off", "position": "center", "start": 4, "duration": 3}
        ],
        "image_slots": 2,
        "effects": ["zoom"],
        "bg_color": (255, 140, 0)
    },
    {
        "id": 5,
        "name": "Event Announcement",
        "description": "Promote upcoming conferences and seminars",
        "transitions": ["slide", "fadeout"],
        "duration": 10,
        "text_slots": [
            {"text": "Join Us at [Event Name]", "position": "center", "start": 1, "duration": 4},
            {"text": "Register Now", "position": "center", "start": 6, "duration": 3}
        ],
        "image_slots": 2,
        "effects": ["fadein"],
        "bg_color": (138, 43, 226)
    },
    {
        "id": 6,
        "name": "Service Showcase",
        "description": "Highlight your professional services",
        "transitions": ["crossfade", "fadein"],
        "duration": 12,
        "text_slots": [
            {"text": "Expert [Service Type]", "position": "center", "start": 2, "duration": 4},
            {"text": "Quality You Can Trust", "position": "center", "start": 7, "duration": 3}
        ],
        "image_slots": 3,
        "effects": ["reintegrate"],
        "bg_color": (46, 139, 87)
    },
    {
        "id": 7,
        "name": "App Demo",
        "description": "Showcase your mobile or web application",
        "transitions": ["zoom", "slide"],
        "duration": 15,
        "text_slots": [
            {"text": "Discover [App Name]", "position": "center", "start": 1, "duration": 4},
            {"text": "Download Today", "position": "center", "start": 10, "duration": 3}
        ],
        "image_slots": 4,
        "effects": ["disintegrate"],
        "bg_color": (72, 209, 204)
    },
    {
        "id": 8,
        "name": "Restaurant Menu",
        "description": "Showcase delicious dishes and specials",
        "transitions": ["fadein", "crossfade"],
        "duration": 12,
        "text_slots": [
            {"text": "Taste the Difference", "position": "center", "start": 2, "duration": 3},
            {"text": "Visit Us Today", "position": "center", "start": 8, "duration": 3}
        ],
        "image_slots": 3,
        "effects": ["zoom"],
        "bg_color": (165, 42, 42)
    },
    {
        "id": 9,
        "name": "Fashion Collection",
        "description": "Display your latest fashion line",
        "transitions": ["slide", "zoom"],
        "duration": 14,
        "text_slots": [
            {"text": "New Collection", "position": "center", "start": 2, "duration": 4},
            {"text": "Shop Now", "position": "center", "start": 9, "duration": 3}
        ],
        "image_slots": 4,
        "effects": ["reintegrate"],
        "bg_color": (199, 21, 133)
    },
    {
        "id": 10,
        "name": "Fitness Program",
        "description": "Promote health and fitness services",
        "transitions": ["zoom", "fadeout"],
        "duration": 10,
        "text_slots": [
            {"text": "Transform Your Life", "position": "center", "start": 1, "duration": 4},
            {"text": "Start Your Journey", "position": "center", "start": 6, "duration": 3}
        ],
        "image_slots": 2,
        "effects": ["fadein"],
        "bg_color": (255, 99, 71)
    }
]

TEXT_PROMPTS = [
    "Generate a promotional video for my [product/service].",
    "Create an ad to introduce our new collection of [clothing/accessories].",
    "Make an exciting ad for the launch of our [mobile app].",
    "Generate a video ad for our [fitness program/online course].",
    "Create a testimonial video to showcase our customers' success stories.",
    "Generate a video to promote our upcoming [sale/discount].",
    "Make a product demo ad for our [electronics product].",
    "Create an event announcement video for our [conference/seminar].",
    "Generate a video ad for our [restaurant/cafe] to showcase our new menu.",
    "Create a holiday promotion video for our [fashion brand].",
    "Make a video showcasing our professional [consulting/advisory] services.",
    "Generate an ad for our [real estate] listings and properties.",
    "Create a video to promote our [automotive] dealership and special offers.",
    "Make a recruitment video for our company to attract top talent.",
    "Generate a video ad for our [beauty/spa] services and treatments.",
    "Create a promotional video for our [travel/tourism] packages.",
    "Make a video showcasing our [educational institution] and programs.",
    "Generate an ad for our [healthcare/medical] services.",
    "Create a video to promote our [charity/nonprofit] cause.",
    "Make a product launch video for our [software/SaaS] platform.",
    "Generate a video showcasing our [home improvement] services.",
    "Create an ad for our [pet care/veterinary] services.",
    "Make a video promoting our [legal/financial] consulting services.",
    "Generate a video ad for our [wedding planning/event] services.",
    "Create a promotional video for our [bakery/catering] business.",
    "Make a video showcasing our [craft/handmade] products.",
    "Generate an ad for our [photography/videography] services.",
    "Create a video to promote our [music/entertainment] venue.",
    "Make a video ad for our [sports/recreation] facility.",
    "Generate a promotional video for our [eco-friendly/sustainable] products.",
    "Create an ad showcasing our [luxury/premium] brand offerings.",
    "Make a video for our [seasonal/limited-time] promotion.",
    "Generate a video ad for our [membership/subscription] program.",
    "Create a promotional video for our [grand opening/launch] event.",
    "Make a video showcasing our [customer loyalty/rewards] program.",
    "Generate an ad for our [delivery/shipping] services.",
    "Create a video promoting our [B2B/wholesale] solutions.",
    "Make a video ad for our [trade show/exhibition] booth.",
    "Generate a promotional video for our [partnership/collaboration] announcement.",
    "Create an ad showcasing our [awards/achievements] and recognition.",
    "Make a video for our [community involvement/CSR] initiatives.",
    "Generate a video ad for our [flash sale/clearance] event.",
    "Create a promotional video for our [webinar/workshop] series.",
    "Make a video showcasing our [innovation/technology] solutions.",
    "Generate an ad for our [franchise/expansion] opportunities.",
    "Create a video promoting our [customer support/service] excellence.",
    "Make a video ad for our [referral/affiliate] program.",
    "Generate a promotional video for our [anniversary/milestone] celebration.",
    "Create an ad showcasing our [before/after] transformation results.",
    "Make a video for our [testimonial/case study] highlights."
]
