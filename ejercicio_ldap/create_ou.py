def create_organizational_unit_ldif(filename, ou_name, base_dn):
    """Creates an LDIF file for an organizational unit."""

    ldif_content = f"""# organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}
"""

    try:
        with open(filename, "w") as f:
            f.write(ldif_content)
        print(f"LDIF file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


def create_multiple_ous_ldif(filename, ou_list, base_dn):
    """Creates an LDIF file for multiple organizational units."""

    try:
        with open(filename, "w") as f:
            for ou_name in ou_list:
                ldif_content = f"""# Organisational unit for {ou_name} department
dn: ou={ou_name},{base_dn}
changetype: add
objectClass: organizationalUnit
ou: {ou_name}

"""
                f.write(ldif_content)

        print(f"LDIF file '{filename}' with multiple OUs created successfully.")
    except Exception as e:
        print(f"Error creating LDIF file '{filename}': {e}")


# Example usage:
filename = "carsi2.ldif"  # Name of the LDIF file
#ou_name = "directores"  # Name of the organizational unit
base_dn = "dc=examencarsi,dc=org"  # Updated base DN

#create_organizational_unit_ldif(filename, ou_name, base_dn)

# Create LDIF file for multiple class groups
class_groups = ["3ESOA", "3ESOB", "3ESOC", "3ESOD", "3ESOE", "3ESOF", "3ESOG","1BACHA", "1BACHB","1BACHC","1BACHD","1BACHE", "GSasir1", "GSasir2", "GSdaw1", "GSdaw2"]
create_multiple_ous_ldif("oueso1khanafer.ldif", class_groups, base_dn)
