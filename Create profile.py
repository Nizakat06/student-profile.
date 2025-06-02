student_profile.txt:
o	def create_profile(name, student_id, bio):
o	    with open('student_profile.txt', 'w') as f:
o	        f.write(f"Name: {name}\n")
o	        f.write(f"Student ID: {student_id}\n")
o	        f.write(f"Bio: {bio}\n")
o	    print("Profile created successfully")
o	
o	if __name__ == "__main__":
o	    create_profile("Nizakat Ali", "22SE06", "I am a student learning software construction.")
o	
