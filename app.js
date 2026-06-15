// app.js - Connecting the Agent to the Dashboard
const jobs = [
    { title: "Solana Smart Contract Review", budget: "500 USDC", platform: "Superteam" },
    { title: "React & Python Developer Needed", budget: "$1200", platform: "Upwork" }
];

function displayJobs() {
    const jobList = document.getElementById('job-list');
    jobList.innerHTML = ''; // Clear previous

    jobs.forEach(job => {
        const jobCard = `
            <div class="card">
                <h4>${job.title}</h4>
                <p>Budget: <strong class="price">${job.budget}</strong> | Platform: ${job.platform}</p>
                <button class="btn" onclick="alert('Proposal successfully sent by AI Agent!')">
                    Send AI Proposal
                </button>
            </div>
        `;
        jobList.innerHTML += jobCard;
    });
}

// Automatically load jobs when page opens
document.addEventListener('DOMContentLoaded', displayJobs);
