# create_command.py

def do_create(self, arg):
    """Create a new instance of a class with parameters."""
    if not arg:
        print("** class name missing **")
        return

    arg_list = arg.split()

    # Extract the class name and remove it from the argument list
    class_name = arg_list[0]

    # Check if the class name is valid
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    # Remove the class name from the argument list
    arg_list.pop(0)

    # Create an empty dictionary to store the attribute key-value pairs
    attr_dict = {}

    # Parse the attributes
    for item in arg_list:
        # Split the item into key and value
        key_value = item.split('=')

        # Check if the item has a valid format
        if len(key_value) != 2:
            continue

        key, value = key_value

        # Remove double quotes and replace underscores with spaces in the value
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]
            value = value.replace('_', ' ')

        # Try to convert the value to an integer or float if possible
        try:
            if '.' in value:
                value = float(value)
            else:
                value = int(value)
        except ValueError:
            pass

        # Add the key-value pair to the attribute dictionary
        attr_dict[key] = value

    # Create a new instance of the class with the parsed attributes
    new_instance = self.classes[class_name](**attr_dict)
    new_instance.save()

    # Print the ID of the newly created instance
    print(new_instance.id)

