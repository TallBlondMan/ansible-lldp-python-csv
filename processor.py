import csv

output_message = ""
with open('netbox_data.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',')
    data_writer.writerow(["device", "name", "type", "enabled"])
    with open("ansible_data") as input_file:
        for line in input_file:
            if line[0] != '}':
                output_message += line 
            else:
                output = output_message.split()

                if output[8].strip("\\\"") != "Inside":
                    device_name = output[1].strip("[]")
                    device_port = output[3].split('=')[1].strip(')')
                    ip_address = output[8].strip("\\\"") + "/24"
                    switch_name = output[10]
                    port_name = output[12].strip("\\\"\\n\"")

                    data_writer.writerow([device_name, device_port, "1000BASE-T (1GE)", "True"])
                else:
                    device_name = output[1].strip("[]")
                    device_port = output[3].split('=')[1].strip(')')
                    internal_connection = "True"

                    data_writer.writerow([device_name, device_port, "Virtual", "True"])

                output_message = ""
