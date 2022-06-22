import interface as inter
import print_contacts as contacts
import find_contact as f
import action_contact as action
import new_contact

def run_programm():
    command = 10
    while command:
        command = inter.main_menu()
        if command == 1: contacts.print_contact()
        elif command == 2:
            finding = inter.get_find()
            print(f"into controller finding: {finding}")
            if finding:
                found = f.find_contact(finding[0], finding[1])
                print(f'into controller found: {found}')
            else:
                continue
            if contacts.print_contact(found) == -1: continue
            action.action_contact(found)
        elif command == 3:
            new_contact_data = inter.get_new_contact()
            if f.exist_contact(new_contact_data):
                if not inter.create_dubl(): continue
            new_contact.create_contact(new_contact_data)
                
