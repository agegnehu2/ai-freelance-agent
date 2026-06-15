# agent_core.py
import os

class FreelanceAgent:
    def __init__(self, dev_name, skills, wallet_address):
        self.dev_name = dev_name
        self.skills = skills
        self.wallet_address = wallet_address
        print(f"[+] AI Agent for {self.dev_name} has started!")
        print(f"[+] Payout Wallet Target: {self.wallet_address}")

    def check_bounties(self):
        """Fetch active Web3 bounties and traditional freelance jobs"""
        available_jobs = [
            {"id": 1, "title": "Solana Smart Contract Review", "budget": "500 USDC", "platform": "Superteam"},
            {"id": 2, "title": "React & Python Developer Needed", "budget": "$1200", "platform": "Upwork"}
        ]
        return available_jobs

    def generate_proposal(self, job_title, budget, platform):
        """Automate tailored proposals for clients"""
        proposal = f"Hello! I am {self.dev_name}. I noticed your project '{job_title}' on {platform}. " \
                   f"With my skills in {', '.join(self.skills)}, I can deliver this perfectly. Please send updates to wallet: {self.wallet_address}."
        return proposal

if __name__ == "__main__":
    # Your live Solana Wallet Address integrated
    YOUR_SOLANA_ADDRESS = "8muWk49hcw1v3GwtAKEF2nDrwVBBbvorky8NJ6kfDjSH"
    
    my_agent = FreelanceAgent(
        dev_name="Agegnehu Shibiru", 
        skills=["JavaScript", "Python", "Web3", "AI"],
        wallet_address=YOUR_SOLANA_ADDRESS
    )
    
    print("\n--- Scanning for Jobs ---")
    jobs = my_agent.check_bounties()
    
    for job in jobs:
        print(f"\n[Job Found] {job['title']} | Budget: {job['budget']} on {job['platform']}")
        print("[Generated Proposal]:")
        print(my_agent.generate_proposal(job['title'], job['budget'], job['platform']))
        
