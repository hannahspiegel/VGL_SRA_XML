#ISSUES TO SOLVE:
#sample submission: https://www.ncbi.nlm.nih.gov/viewvc/v1/trunk/submit/public-docs/sra/samples/sra.submission.run.xml?view=co

# dummy filepath: /Users/hannahspiegel/Desktop/VGL/fAnaTes1_files.txt

# Opening the file with absolute path
filepath = "/Users/hannahspiegel/Desktop/VGL/fAnaTes1_files.txt"

# Create empty list and fill it by iterating over the lines of the filepaths doc
path_list = []
with open(filepath, 'r') as file:
    line = file.readlines()
    for i in line:
        if len(i) > 2:
            path_list.append(i.strip())
            
# Make this a loop over path_list:
from pathlib import Path

paths = []
part = ''
p = []

for i in path_list:
    path = Path(i).parts
    paths.append(path) # Append path to the paths list

    list(path)
    if len(path) > 1:
        (path[2])
 
# create library_name and save as list
tolid = []

for path in paths: 
    if len(path) > 1:
        tolid.append(path[2])

instrument = []
for path in paths:
    if len(path) > 1:
        instrument.append(path[4])

# merge instrument and tolid and add incremental number for each item on list to create unique library ID 
library_name_list = []
def merge(list1, list2): 
    if len(i) > 1:
        merged_list = [(list1[i]+"_"+list2[i]+"_"+str(i+1)) for i in range(0, len(list1))]
        return list(merged_list)

library_name_list = merge(tolid,instrument) 


# define library_strategy and save as list:
library_strategy_list = []

for path in paths: 
    if len(path) > 1:
        if '10x' in path:
            library_strategy_list.append("WGS")
        elif 'arima' in path: 
            library_strategy_list.append("Hi-C")
        elif 'dovetail' in path:
            library_strategy_list.append("Hi-C")
        elif 'illumina' in path:
            library_strategy_list.append("Hi-C")
        elif 'pacbio' in path: 
            library_strategy_list.append("WGS")
        else: 
            library_strategy_list.append("check filepath")


# define library_source and save as list
library_source_list = []

for path in paths: 
    if len(path) > 1: 
        library_source_list.append('GENOMIC')

       
# define library_selection and save as list 
library_selection_list = []
    
for path in paths:
    if len(path) > 1: 
        if '10x' in path:
            library_selection_list.append("RANDOM")
        elif 'arima' in path: 
            library_selection_list.append("Restriction Digest")
        elif 'dovetail' in path:
            library_selection_list.append("Restriction Digest")
        elif 'illumina' in path:
            library_selection_list.append("Restriction Digest")
        elif 'pacbio' in path: 
            library_selection_list.append("size fractionation")
        else: 
            library_selection_list.append("check filepath")


# Define library_layout and save as a list
library_layout_list = []

for path in paths: 
    if len(path) > 1:
        if '10x' in path:
            library_layout_list.append("paired")
        elif 'arima' in path: 
            library_layout_list.append("paired")
        elif 'dovetail' in path:
            library_layout_list.append("paired")
        elif 'illumina' in path:
            library_layout_list.append("paired")
        elif 'pacbio' in path: 
            library_layout_list.append("single")
        else: 
            library_layout_list.append("check filepath")

def verify_paired_layout(paths):
    pe = False
    for current, next_path in zip(paths, paths[1:]):
        if current[-1] == "1" and next_path[-1] == "2":
            if pe:
                return False
            pe = True
        elif current[-1] == next_path[-1]:
            continue
        else:
            return False
    return pe
    
paired_end_list = [verify_paired_layout(path) for path in paths]
       
# Define platform and save as list 
platform_list = []

for path in paths: 
    if len(path) > 1:
        if '10x' in path:
            platform_list.append("ILLUMINA")
        elif 'arima' in path: 
            platform_list.append("ILLUMINA")
        elif 'dovetail' in path:
            platform_list.append("ILLUMINA")
        elif 'illumina' in path:
            platform_list.append("ILLUMINA")
        elif 'pacbio' in path:
            platform_list.append("PACBIO_SMRT")
        else: 
            platform_list.append("check filepath")

            
# Define instrument_model and save as list 
instrument_model_list = []

for path in paths: 
    if len(path) > 1:
        if '10x' in path:
            instrument_model_list.append("Illumina NovaSeq 6000")
        elif 'arima' in path: 
            instrument_model_list.append("Illumina NovaSeq 6000")
        elif 'dovetail' in path:
            instrument_model_list.append("Illumina NovaSeq 6000")
        elif 'illumina' in path:
            instrument_model_list.append("Illumina NovaSeq 6000")
        elif 'pacbio' in path: 
            instrument_model_list.append("PacBio Sequel II")
        else: 
            instrument_model_list.append("check filepath")

            
# Define library_construction_protocol and save as list
library_construction_protocol_list = []

for path in paths:
    if len(path) > 1: 
        if '10x' in path:
            library_construction_protocol_list.append("manufacturer's protocol")
        elif 'arima' in path: 
            library_construction_protocol_list.append("manufacturer's protocol")
        elif 'dovetail' in path:
            library_construction_protocol_list.append("manufacturer's protocol")
        elif 'illumina' in path:
            library_construction_protocol_list.append("manufacturer's protocol")
        elif 'pacbio' in path: 
            library_construction_protocol_list.append("SAGE blue pippin")
        else: 
            library_construction_protocol_list.append("check filepath")
            
# First part of the XML doc 
# can we include a second email? 
# comment is optional field, leave empty
"""xml_intro = 
<Submission>
    <Description>
        <Comment></Comment>
        <Organization role="owner" type="institute">
            <Name>Vertebrate Genome Project</Name>
            <Contact email="ejarvis@rockefeller.edu">
                <Name>
                    <First>Erich</First>
                    <Last>Jarvis</Last>
                </Name>
            </Contact>
        </Organization>
        <Hold release_date=""/>
    </Description>"""


import xml.etree.ElementTree as ET #fix this to use Jinja2

# Read and parse the XML template

xml_string = '''
    <Action>
        <AddFiles target_db="SRA">
            <File file_path="">
                <DataType>generic-data</DataType>
            </File>
            <Attribute name="instrument_model"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_name"></Attribute>
            <Attribute name="library_strategy"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_source"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_selection"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_layout"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_construction_protocol"></Attribute>
            <AttributeRefId name="BioProject">
                <RefId>
                    <PrimaryId db="BioProject"></PrimaryId>
                </RefId>
            </AttributeRefId>
            <AttributeRefId name="BioSample">
                <RefId>
                    <PrimaryId db="BioSample"></PrimaryId>
                </RefId>
            </AttributeRefId>
            <Identifier>
                <SPUID spuid_namespace="CFSAN">VGL</SPUID>
            </Identifier>
        </AddFiles>
    </Action>

    '''
# read and parse second XML template for paired reads

xml_string_pair = '''
    <Action>
        <AddFiles target_db="SRA">
            <File file_path="">
                <DataType>generic-data</DataType>
            </File>
            <File file_path="">
                <DataType>generic-data</DataType>
            </File>
            <Attribute name="instrument_model"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_name"></Attribute>
            <Attribute name="library_strategy"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_source"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_selection"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_layout"></Attribute>
            <!--  controlled vocabulary  -->
            <Attribute name="library_construction_protocol"></Attribute>
            <AttributeRefId name="BioProject">
                <RefId>
                    <PrimaryId db="BioProject"></PrimaryId>
                </RefId>
            </AttributeRefId>
            <AttributeRefId name="BioSample">
                <RefId>
                    <PrimaryId db="BioSample"></PrimaryId>
                </RefId>
            </AttributeRefId>
            <Identifier>
                <SPUID spuid_namespace="CFSAN"></SPUID>
            </Identifier>
        </AddFiles>
    </Action>
    
    '''
import csv

csv_file = "/Users/hannahspiegel/Desktop/VGL/venv/UMBRELLA_BIOPROJECT_ID.csv"

# Create an empty dictionary to store the data
bioproject_dict = {}

# Read the CSV file and populate the dictionary
with open(csv_file, "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if len(row) >= 2:  # Make sure the row has at least 3 columns
            key = row[0]
            value1 = row[1]
            value2 = row[2]
            bioproject_dict[key] = (value1, value2)


# function to fill the xml doc (single library_layout)
import uuid

#prompt user for BioSample ID
biosample_value = input("Enter BioSample value for the submission: ")

def fill_xml(xml_string, n, biosample_value):

    root = ET.fromstring(xml_string)
  
    # Define the data to fill in the XML
    data = { 
        'file_path': path_list[n],
        'instrument_model': instrument_model_list[n],
        'library_name': library_name_list[n],
        'library_strategy': library_strategy_list[n],
        'library_source': library_source_list[n],
        'library_selection': library_selection_list[n],
        'library_layout': library_layout_list[n],
        'library_construction_protocol': library_construction_protocol_list[n],
#       'BioProject': 'PRJ12345',
        'BioProject': bioproject_dict.get(tolid[n], ("", ""))[0],  # Get BioProject value from the dictionary
        'BioSample': biosample_value
    }

    # Fill in the XML elements with data
    file_path_element = root.find("./AddFiles/File")
    file_path_element.set('file_path', data['file_path'])

    attribute_names = [
        'instrument_model',
        'library_name',
        'library_strategy', 
        'library_source',
        'library_selection',
        'library_layout',
        'library_construction_protocol'
    ]

    for attr_name in attribute_names:
        attribute_element = root.find(f"./AddFiles/Attribute[@name='{attr_name}']")
        attribute_element.text = data[attr_name]

    attr_ref_ids = ['BioProject', 'BioSample']

    for ref_id_name in attr_ref_ids:
        ref_id_element = root.find(f"./AddFiles/AttributeRefId[@name='{ref_id_name}']/RefId/PrimaryId")
        ref_id_element.text = data[ref_id_name]
        
        identifier_element = root.find("./AddFiles/Identifier/SPUID")
        identifier_element.text = str(uuid.uuid4())  # Generates a random UUID
    
    if tolid[n] in bioproject_dict:
        bioproject_value = bioproject_dict[tolid[n]][0]  # Assuming the first value from the tuple
        ref_id_element = root.find("./AddFiles/AttributeRefId[@name='BioProject']/RefId/PrimaryId")
        ref_id_element.text = bioproject_value

    # Convert the updated XML back to a string
    updated_xml_string = ET.tostring(root, encoding='unicode')

    return(updated_xml_string) #switch this to append to xml file

#fill_xml(xml_string, 1)

#function to fill xml (paired library_layout) 
def fill_xml_paired(xml_string_pair, n, biosample_value):

    root = ET.fromstring(xml_string_pair)

    # Define the data to fill in the XML
    data = { 
        'file_path': path_list[n],
        'file_path_2':path_list[n+1],
        'instrument_model': instrument_model_list[n],
        'library_name': library_name_list[n],
        'library_strategy': library_strategy_list[n],
        'library_source': library_source_list[n],
        'library_selection': library_selection_list[n],
        'library_layout': library_layout_list[n],
        'library_construction_protocol': library_construction_protocol_list[n],
#       'BioProject': 'PRJ12345',
        'BioProject': bioproject_dict.get(tolid[n], ("", ""))[0],  # Get BioProject value from the dictionary
        'BioSample': biosample_value
    }

    # Fill in the XML elements with data
    file_path_elements = root.findall("./AddFiles/File")

    # Update the first file_path
    file_path_element = file_path_elements[0]
    file_path_element.set('file_path', data['file_path'])

    # Update the second file_path
    file_path_element = file_path_elements[1]
    file_path_element.set('file_path', data['file_path_2'])

    attribute_names = [
        'instrument_model',
        'library_name',
        'library_strategy', 
        'library_source',
        'library_selection',
        'library_layout',
        'library_construction_protocol'
    ]

    for attr_name in attribute_names:
        attribute_element = root.find(f"./AddFiles/Attribute[@name='{attr_name}']")
        attribute_element.text = data[attr_name]

    attr_ref_ids = ['BioProject', 'BioSample']

    for ref_id_name in attr_ref_ids:
        ref_id_element = root.find(f"./AddFiles/AttributeRefId[@name='{ref_id_name}']/RefId/PrimaryId")
        ref_id_element.text = data[ref_id_name]

        identifier_element = root.find("./AddFiles/Identifier/SPUID")
        identifier_element.text = str(uuid.uuid4())  # Generates a random UUID

    # Convert the updated XML back to a string
    updated_xml_string = ET.tostring(root, encoding='unicode')

    return updated_xml_string


    # Initialize the final XML content
final_xml_content = ""

def run_filling():
    global final_xml_content
    # Iterate through each pair of paths (for paired reads)
    for n in range(0, len(path_list), 2):
        if library_layout_list[n] == "single":
            xml_filled = fill_xml(xml_string, n, biosample_value)
        elif n + 1 < len(path_list) and library_layout_list[n] == "paired" and library_layout_list[n + 1] == "paired":
            xml_filled = fill_xml_paired(xml_string_pair, n, biosample_value)
        else:
            raise ValueError(f"Invalid layout configuration at index {n}: {library_layout_list[n:n+2]}")

        # Append the filled XML to the final XML content
        final_xml_content += "\n\t" + xml_filled

# Prompt the user for BioSample value
run_filling()

# Opening elements for XML document
xml_intro = '''<Submission>
    <Description>
        <Comment>GS - BP(1.0)+BS(1.0)+SRA</Comment>
        <Organization role="owner" type="institute">
            <Name>Vertebrate Genome Project</Name>
            <Contact email="ejarvis@rockefeller.edu">
                <Name>
                    <First>Erich</First>
                    <Last>Jarvis</Last>
                </Name>
            </Contact>
        </Organization>
        <Hold release_date=""/>
    </Description>
'''
# Append the closing elements to the resulting XML document

closing_elements = '''
</Submission>
'''
# Combine the XML introduction, content, and closing elements 

final_xml = xml_intro + final_xml_content + closing_elements

# Perform actions with the final XML content or save it to a file

print(final_xml) 

# Define the ToLID for the filename

tolid_for_filename = tolid[0]

# Define the filename

filename = f"{tolid_for_filename}_SRA_metadata.xml"

# Save the final XML content to a file

with open(filename, 'w') as file:
    file.write(final_xml)

#print(f"XML content saved to {filename}")