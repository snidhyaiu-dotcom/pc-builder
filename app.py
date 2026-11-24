from flask import Flask, render_template, request
from urllib.parse import quote_plus

app = Flask(__name__)

# Replace 'yourtag-21' with your actual Amazon Associates Tracking ID
AMAZON_TAG = "yourtag-21"

def amazon_link(part_name):
    query = quote_plus(part_name)
    return f"https://amazon.in{query}&tag={AMAZON_TAG}"

PC_BUILDS = {
    "gaming": {
        "budget": {
            "name": "1080p Entry Gaming PC",
            "cpu": "AMD Ryzen 5 5600",
            "gpu": "AMD Radeon RX 6600 8GB",
            "ram": "16GB DDR4 3200MHz",
            "storage": "1TB NVMe SSD",
            "psu": "550W 80+ Bronze",
            "est_price": "₹55,000"
        },
        "mid": {
            "name": "1440p High-Refresh Gaming PC",
            "cpu": "AMD Ryzen 5 7600",
            "gpu": "NVIDIA RTX 4070 Super",
            "ram": "32GB DDR5 6000MHz",
            "storage": "1TB NVMe Gen4 SSD",
            "psu": "750W 80+ Gold",
            "est_price": "₹1,15,000"
        },
        "high": {
            "name": "4K Ultra Gaming Beast",
            "cpu": "AMD Ryzen 7 7800X3D",
            "gpu": "NVIDIA RTX 4080 Super",
            "ram": "32GB DDR5 6000MHz",
            "storage": "2TB NVMe Gen4 SSD",
            "psu": "850W 80+ Gold",
            "est_price": "₹1,90,000"
        }
    },
    "work": {
        "budget": {
            "name": "Smooth Office & Daily Work PC",
            "cpu": "Intel Core i3-12100",
            "gpu": "Integrated Intel UHD 730",
            "ram": "16GB DDR4 3200MHz",
            "storage": "512GB NVMe SSD",
            "psu": "450W 80+ Bronze",
            "est_price": "₹32,000"
        },
        "mid": {
            "name": "Heavy Multitasking & Coding PC",
            "cpu": "Intel Core i5-13500",
            "gpu": "Integrated Intel UHD 770",
            "ram": "32GB DDR5",
            "storage": "1TB NVMe Gen4 SSD",
            "psu": "550W 80+ Gold",
            "est_price": "₹58,000"
        },
        "high": {
            "name": "Pro Workstation & Data Rig",
            "cpu": "AMD Ryzen 9 7900",
            "gpu": "NVIDIA RTX 4060 8GB",
            "ram": "64GB DDR5",
            "storage": "2TB NVMe Gen4 SSD",
            "psu": "650W 80+ Gold",
            "est_price": "₹1,25,000"
        }
    },
    "editing": {
        "budget": {
            "name": "1080p Video & Photo Editing PC",
            "cpu": "Intel Core i5-12400F",
            "gpu": "NVIDIA RTX 3060 12GB",
            "ram": "32GB DDR4",
            "storage": "1TB NVMe SSD",
            "psu": "650W 80+ Bronze",
            "est_price": "₹65,000"
        },
        "mid": {
            "name": "4K Video Editing & Blender PC",
            "cpu": "Intel Core i7-14700K",
            "gpu": "NVIDIA RTX 4070 12GB",
            "ram": "32GB DDR5",
            "storage": "2TB NVMe Gen4 SSD",
            "psu": "750W 80+ Gold",
            "est_price": "₹1,35,000"
        },
        "high": {
            "name": "Studio 3D & AI Workhorse",
            "cpu": "AMD Ryzen 9 7950X",
            "gpu": "NVIDIA RTX 4090 24GB",
            "ram": "64GB DDR5",
            "storage": "4TB NVMe Gen4 SSD",
            "psu": "1000W 80+ Platinum",
            "est_price": "₹2,80,000"
        }
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_build = None
    links = {}
    use_case = "gaming"
    budget = "mid"

    if request.method == "POST":
        use_case = request.form.get("use_case")
        budget = request.form.get("budget")
        selected_build = PC_BUILDS.get(use_case, {}).get(budget)
        if selected_build:
            links = {
                "cpu": amazon_link(selected_build["cpu"]),
                "gpu": amazon_link(selected_build["gpu"]),
                "ram": amazon_link(selected_build["ram"]),
                "storage": amazon_link(selected_build["storage"]),
                "psu": amazon_link(selected_build["psu"]),
            }

    return render_template(
        "index.html",
        build=selected_build,
        links=links,
        use_case=use_case,
        budget=budget
    )

if __name__ == "__main__":
    app.run(debug=True)
