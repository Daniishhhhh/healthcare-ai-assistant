// ===============================
// Swasthya Setu Helplines Loader
// ===============================

document.addEventListener("DOMContentLoaded", loadHelplines);

async function loadHelplines() {

    console.log("Loading helplines...");

    try {

        // ✅ Correct path relative to helplines.html
        const response = await fetch("data/helplines.json");

        if (!response.ok) {
            throw new Error("Failed to load JSON file");
        }

        const data = await response.json();

        console.log("Helplines data:", data);

        const grid = document.getElementById("helplineGrid");

        if (!grid) {
            console.error("❌ helplineGrid element not found in HTML");
            return;
        }

        // Clear loading text if present
        grid.innerHTML = "";

        if (!Array.isArray(data) || data.length === 0) {
            grid.innerHTML = "<p>No helpline data available.</p>";
            return;
        }

        // ===============================
        // Create Cards
        // ===============================
        data.forEach(item => {

            const card = document.createElement("div");
            card.className = "card";

            const number = item.number || "N/A";

            card.innerHTML = `
                <h3>${item.name || "Helpline"}</h3>

                <div class="number">
                    ${number}
                </div>

                <div class="desc">
                    ${item.description || ""}
                </div>

                <a class="call-btn" href="tel:${number}">
                    📞 Call Now
                </a>
            `;

            grid.appendChild(card);

        });

        console.log("✅ Helplines loaded successfully");

    } catch (error) {

        console.error("❌ Helpline load error:", error);

        const grid = document.getElementById("helplineGrid");

        if (grid) {
            grid.innerHTML = `
                <p style="color:red;">
                    Error loading helplines. Please check JSON path.
                </p>
            `;
        }
    }
}
