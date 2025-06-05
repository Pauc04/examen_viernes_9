def create_students_ldif(class_name, num_students, filename, base_dn):
    """Generates an LDIF file with a specified number of students for a given class."""
    ldif_content = ""

    for i in range(1, num_students + 1):
        username = f"student{i}"
        ldif_content += f"""# Student {i} in {class_name}
dn: uid={username},ou={class_name},{base_dn}
changetype: add
objectClass: inetOrgPerson
cn: Student{i} Name
sn: Student{i}
uid: {username}
userPassword: password{i}

"""

    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully with {num_students} students in {class_name}.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "carsi2.ldif"   # Output LDIF file
base_dn = "dc=examencarsi,dc=org"           # Your base DN
class_name = "alumnos"                     # Class name
num_students = 472                        # Number of students

create_students_ldif(class_name, num_students, filename, base_dn)
