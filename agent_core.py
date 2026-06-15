# agent_core.py
import os

class FreelanceAgent:
    def __init__(self, dev_name, skills):
        self.dev_name = dev_name
        self.skills = skills
        print(f"[+] AI Agent for {self.dev_name} has started!")

    def check_bounties(self):
        """Fetch active Web3 bounties and traditional freelance jobs"""
        # Mock data for testing (Will be replaced with real APIs later)
        available_jobs = [
            {"id": 1, "title": "Solana Smart Contract Review", "budget": "500 USDC", "platform": "Superteam"},
            {"id": 2, "title": "React & Python Developer Needed", "budget": "$1200", "platform": "Upwork"}
        ]
        return available_jobs

    def generate_proposal(self, job_title, budget, platform):
        """Automate tailored proposals for clients"""
        proposal = f"Hello! I am {self.dev_name}. I noticed your project '{job_title}' on {platform}. " \
                   f"With my skills in {', '.join(self.skills)}, I can deliver this perfectly within your budget of {budget}."
        return proposal

if __name__ == "__main__":
    # Initialize the agent with your profile
    my_agent = FreelanceAgent(dev_name="Agegnehu Shibiru", skills=["JavaScript", "Python", "Web3", "AI"])
    
    print("\n--- Scanning for Jobs ---")
    jobs = my_agent.check_bounties()
    
    for job in jobs:
        print(f"\n[Job Found] {job['title']} | Budget: {job['budget']} on {job['platform']}")
        print("[Generated Proposal]:")
        print(my_agent.generate_proposal(job['title'], job['budget'], job['platform']))
      
