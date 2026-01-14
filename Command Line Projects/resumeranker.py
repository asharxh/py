import os
import csv

def load_resumes(filename="resumes.txt"):
    resumes = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    name, skills, experience, education, certs = parts
                    resumes.append({
                        "name": name,
                        "skills": skills.split(",") if skills else [],
                        "experience": float(experience),
                        "education": education,
                        "certifications": certs.split(",") if certs else []
                    })
    return resumes

def save_resumes(resumes, filename="resumes.txt"):
    with open(filename, "w") as f:
        for r in resumes:
            f.write(f"{r['name']}|{','.join(r['skills'])}|{r['experience']}|{r['education']}|{','.join(r['certifications'])}\n")

def calculate_score(resume):
    score = 0
    score += resume["experience"] * 2
    edu_weights = {"PhD": 10, "Masters": 8, "Bachelors": 6, "Diploma": 4, "High School": 2}
    score += edu_weights.get(resume["education"], 0)
    score += len(resume["skills"]) * 3
    score += len(resume["certifications"]) * 2
    return score

def display_resume(resume, score=None):
    print(f"Name: {resume['name']}")
    print(f"Skills: {', '.join(resume['skills'])}")
    print(f"Experience: {resume['experience']} years")
    print(f"Education: {resume['education']}")
    print(f"Certifications: {', '.join(resume['certifications'])}")
    if score is not None:
        print(f"Score: {score}")
    print("-"*50)

def export_top_candidates(resumes, top_n=5, filename="top_candidates.csv"):
    ranked = sorted(resumes, key=lambda x: calculate_score(x), reverse=True)[:top_n]
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name", "Skills", "Experience", "Education", "Certifications", "Score"])
        for r in ranked:
            writer.writerow([r["name"], ",".join(r["skills"]), r["experience"], r["education"], ",".join(r["certifications"]), calculate_score(r)])
    print(f"Top {top_n} candidates exported to '{filename}'.")

def resume_ranker_advanced():
    resumes = load_resumes()

    while True:
        print("\n--- Advanced Resume Ranker CLI ---")
        print("1. Add Resume")
        print("2. View All Resumes")
        print("3. Search Resume")
        print("4. Filter Resumes")
        print("5. Rank Resumes")
        print("6. Export Top Candidates to CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter candidate name: ")
            skills = input("Enter skills (comma separated): ").split(",")
            experience_input = input("Enter years of experience: ")
            education = input("Enter highest education (PhD/Masters/Bachelors/Diploma/High School): ")
            certs = input("Enter certifications (comma separated, if any): ").split(",") if input("Add certifications? (y/n): ").lower()=="y" else []
            if not experience_input.replace(".","",1).isdigit():
                print("Invalid experience.")
                continue
            resumes.append({
                "name": name,
                "skills": [s.strip() for s in skills],
                "experience": float(experience_input),
                "education": education.strip(),
                "certifications": [c.strip() for c in certs if c]
            })
            save_resumes(resumes)
            print(f"Resume for '{name}' added successfully.")

        elif choice == "2":
            if not resumes:
                print("No resumes available.")
                continue
            for r in resumes:
                display_resume(r, calculate_score(r))

        elif choice == "3":
            keyword = input("Enter candidate name to search: ").lower()
            found = False
            for r in resumes:
                if keyword in r["name"].lower():
                    display_resume(r, calculate_score(r))
                    found = True
            if not found:
                print("No matching candidate found.")

        elif choice == "4":
            min_exp_input = input("Minimum experience (years, leave blank to skip): ")
            required_skills = input("Required skills (comma separated, leave blank to skip): ").split(",") if input("Filter by skills? (y/n): ").lower() == "y" else []
            min_exp = float(min_exp_input) if min_exp_input.replace(".","",1).isdigit() else 0
            filtered = []
            for r in resumes:
                if r["experience"] >= min_exp and all(skill.strip().lower() in [s.lower() for s in r["skills"]] for skill in required_skills if skill):
                    filtered.append(r)
            if not filtered:
                print("No resumes match the filter criteria.")
            else:
                print(f"Filtered Resumes ({len(filtered)} found):")
                for r in filtered:
                    display_resume(r, calculate_score(r))

        elif choice == "5":
            if not resumes:
                print("No resumes available.")
                continue
            ranked = sorted(resumes, key=lambda x: calculate_score(x), reverse=True)
            print("Resumes Ranked:")
            for idx, r in enumerate(ranked, start=1):
                print(f"Rank {idx}:")
                display_resume(r, calculate_score(r))

        elif choice == "6":
            top_n_input = input("Enter number of top candidates to export (default 5): ")
            top_n = int(top_n_input) if top_n_input.isdigit() else 5
            export_top_candidates(resumes, top_n)

        elif choice == "7":
            print("Exiting Advanced Resume Ranker.")
            break

        else:
            print("Invalid choice. Please select again.")

resume_ranker_advanced()