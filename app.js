// app.js - Fetching Real Live Crypto/Web3 Gigs
async function fetchLiveJobs() {
    const jobList = document.getElementById('job-list');
    jobList.innerHTML = '<p>Scanning the blockchain and job boards...</p>';

    try {
        // Fetch active data from a public Web3/Crypto jobs API
        const response = await fetch('https://remoteok.com/api?tag=crypto');
        const data = await response.json();
        
        // Take the first 3 latest jobs from the API response
        const liveJobs = data.slice(1, 4); 
        jobList.innerHTML = ''; 

        liveJobs.forEach(job => {
            const jobCard = `
                <div class="card">
                    <h4>${job.position}</h4>
                    <p>Company: <strong>${job.company}</strong></p>
                    <p>Platform: <span class="status">Remote Web3</span></p>
                    <button class="btn" onclick="alert('AI Agent is analyzing this job and writing a custom proposal...')">
                        Auto-Apply with AI
                    </button>
                </div>
            `;
            jobList.innerHTML += jobCard;
        });
    } catch (error) {
        jobList.innerHTML = '<p style="color:red;">Error connecting to live job boards. Retrying...</p>';
    }
}

document.addEventListener('DOMContentLoaded', fetchLiveJobs);
