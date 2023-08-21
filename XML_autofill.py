#ISSUES TO SOLVE:

#need to work out a way to grab the biosample ID from NCBI, under assemblies
#sample submission: https://www.ncbi.nlm.nih.gov/viewvc/v1/trunk/submit/public-docs/sra/samples/sra.submission.run.xml?view=co

# test filepath: /Users/hannahspiegel/Desktop/VGL/fAnaTes1_files.txt
import uuid
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

species = []
for path in paths:
    if len(path) > 1:
        species.append(path[1])

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

#create a dictionary of existing BioProject ID numbers:

data = '''Acanthisitta_chloris	PRJNA562166
Acanthopagrus_latus	PRJEB40702
Accipiter_gentilis	PRJEB48396
Acipenser_ruthenus	PRJEB35914
Acomys_russatus	PRJEB39769
Acridotheres_tristis	PRJNA922139
Alca_torda	PRJNA566188
Alosa_sapidissima	PRJNA776885
Amblyraja_radiata	PRJNA593039
Ammodytes_marinus	PRJEB60704
Ammospiza_caudacuta	PRJNA922976
Ammospiza_nelsoni	PRJNA922164
Anabas_testudineus	PRJEB30393
Anableps_anableps	PRJNA562167
Anas_acuta	PRJEB64746
Anas_platyrhynchos	PRJNA641113
Anguilla_anguilla	PRJNA562168
Antennarius_maculatus	PRJNA562173
Aplochiton_taeniatus	PRJNA562176
Apodemus_sylvaticus	PRJEB53556
Apus_apus	PRJNA776865
Aquila_chrysaetos_chrysaetos	PRJEB33202
Ara_ararauna	PRJNA935292
Archocentrus_centrarchus	PRJNA533105
Argentina_silus	PRJEB59966
Arvicanthis_niloticus	PRJNA562178
Arvicola_amphibius	PRJEB39551
Astatotilapia_calliptera	PRJNA557691
Asterias_rubens	PRJEB33975
Aythya_fuligula	PRJNA562180
Balaenoptera_acutorostrata	PRJEB60647
Balaenoptera_musculus	PRJNA557693
Balaenoptera_ricei	PRJNA927325
Balearica_regulorum_gibbericeps	PRJNA562181
Barbatula_barbatula	PRJEB55341
Barbus_barbus	PRJEB51453
Betta_splendens	PRJEB30367
Bombina_bombina	PRJNA922148
Borostomias_antarcticus	PRJEB60198
Bos_indicus_x_Bos_taurus	PRJNA603765
Bucorvus_abyssinicus	PRJNA562182
Bufo_bufo	PRJEB42238
Callithrix_jacchus	PRJNA560230
Calypte_anna	PRJNA510144
Canis_lupus	PRJEB43409
Caprimulgus_europaeus	PRJEB44830
Carassius_carassius	PRJEB62001
Carcharodon_carcharias	PRJNA562191
Cariama_cristata	PRJNA562192
Catharus_ustulatus	PRJNA562193
Cervus_elaphus	PRJEB45171
Chanos_chanos	PRJEB33883
Chelmon_rostratus	PRJNA562194
Chelon_labrosus	PRJEB63499
Chelonia_mydas	PRJNA562195
Chionomys_nivalis	PRJEB59810
Chiroxiphia_lanceolata	PRJNA562196
Choloepus_didactylus	PRJNA562198
Ciconia_maguari	PRJNA717215
Cinclus_cinclus	PRJEB61999
Colius_striatus	PRJNA938129
Corella_eumyota	PRJEB59956
Corvus_hawaiiensis	PRJNA776866
Corvus_moneduloides	PRJNA561795
Cottoperca_gobio	PRJEB30272
Cuculus_canorus	PRJNA562200
Cyclopterus_lumpus	PRJNA562201
Cyclura_pinguis	PRJNA986166
Cygnus_olor	PRJNA562205
Cynocephalus_volans	PRJNA913149
Danio_rerio	PRJEB38590
Danio_rerio	PRJEB52651
Dasypus_novemcinctus	PRJNA993262
Delphinus_delphis	PRJEB60667
Dendropsophus_ebraccatus	PRJNA922582
Denticeps_clupeoides	PRJEB31550
Dermochelys_coriacea	PRJNA562206
Diceros_bicornis_minor	PRJNA776883
Discoglossus_pictus	PRJNA915386
Dromaius_novaehollandiae	PRJNA641107
Dromiciops_gliroides	PRJNA776875
Dryobates_pubescens	PRJNA562232
Dugong_dugon	PRJNA970804
Echeneis_naucrates	PRJEB31994
Electrona_antarctica	PRJEB60649
Electrona_carlsbergi	PRJEB63513
Electrona_subaspera	PRJEB63623
Electrophorus_electricus	PRJNA562207
Elephas_maximus_indicus	PRJNA855931
Emys_orbicularis	PRJNA927029
Eptesicus_nilssonii	PRJEB61925
Erethizon_dorsatum	PRJNA927022
Erinaceus_europaeus	PRJEB60669
Erithacus_rubecula	PRJEB38659
Erpetoichthys_calabaricus	PRJEB31587
Eschrichtius_robustus	PRJNA927345
Esox_lucius	PRJNA562208
Eubalaena_glacialis	PRJNA932450
Euleptes_europaea	PRJNA935365
Eutrigla_gurnardus	PRJEB64070
Falco_biarmicus	PRJNA844077
Falco_cherrug	PRJNA844067
Falco_naumanni	PRJNA715196
Falco_peregrinus	PRJNA844070
Falco_punctatus	PRJEB61047
Falco_rusticolus	PRJNA562209
Fringilla_coelebs	PRJEB61919
Gadus_morhua	PRJEB33456
Gallus_gallus	PRJNA673216
Gallus_gallus	PRJNA915401
Gallus_gallus	PRJNA915403
Gasterosteus_aculeatus	PRJEB62003
Gastrophryne_carolinensis	PRJNA923362
Gavialis_gangeticus	PRJNA972737
Geothlypis_trichas	PRJNA593040
Geotrypetes_seraphini	PRJEB33993
Girardinichthys_multiradiatus	PRJNA895397
Gobio_gobio	PRJEB59786
Gobius_niger	PRJEB61917
Gopherus_evgoodei	PRJNA533104
Gopherus_flavomarginatus	PRJNA842024
Gouania_willdenowi	PRJEB30363
Grus_americana	PRJNA938116
Gymnoscopelus_braueri	PRJEB64710
Gypaetus_barbatus	PRJNA927017
Haemorhous_mexicanus	PRJNA915091
Haliaeetus_albicilla	PRJEB57284
Harpia_harpyja	PRJNA903882
Hemiprocne_comata	PRJNA776867
Hemiscyllium_ocellatum	PRJNA776876
Heterohyrax_brucei	PRJNA932717
Hippoglossus_hippoglossus	PRJNA562210
Hippopotamus_amphibius_kiboko	PRJNA972732
Hipposideros_larvatus	PRJNA776886
Hirundo_rustica	PRJNA641117
Homo_sapiens	PRJNA562213
Hoplias_malabaricus	PRJNA952991
Hyla_sarda	PRJNA945447
Hypanus_sabinus	PRJNA976741
Hyperoodon_ampullatus	PRJEB60010
Hyperoplus_immaculatus	PRJEB58244
Jaculus_jaculus	PRJNA776884
Kogia_breviceps	PRJNA903912
Labrus_mixtus	PRJEB63507
Lacerta_agilis	PRJNA562214
Lagenorhynchus_albirostris	PRJEB60663
Lagopus_muta	PRJNA843060
Lampris_incognitus	PRJNA952990
Lemur_catta	PRJNA562215
Loxodonta_africana	PRJNA970377
Lutra_lutra	PRJEB35340
Lycodopsis_pacificus	PRJNA928479
Lynx_canadensis	PRJNA533103
Malaclemys_terrapin_pileata	PRJNA923333
Manis_pentadactyla	PRJNA972736
Mastacembelus_armatus	PRJEB31554
Megalops_cyprinoides	PRJNA562216
Melanostigma_gelatinosum	PRJEB59776
Melanotaenia_boesemani	PRJNA562218
Meles_meles	PRJEB46333
Melopsittacus_undulatus	PRJNA562220
Melospiza_georgiana	PRJNA927021
Merops_nubicus	PRJNA562222
Mesoplodon_densirostris	PRJNA875937
Microcaecilia_unicolor	PRJEB32739
Microchirus_variegatus	PRJEB64068
Mobula_birostris	PRJNA954412
Molossus_molossus	PRJNA674390
Monodelphis_domestica	PRJNA922994
Mus_musculus	PRJEB59719
Mustela_erminea	PRJNA562223
Mustela_lutreola	PRJNA986837
Myotis_daubentonii	PRJEB61137
Myotis_myotis	PRJNA674393
Myripristis_murdjan	PRJEB33189
Nansenia_antarctica	PRJEB64098
Neoarius_graeffei	PRJNA922166
Neofelis_nebulosa	PRJNA927027
Nesoenas_mayeri	PRJEB64092
Notamacropus_eugenii	PRJNA928718
Notolabrus_celidotus	PRJNA562225
Notothenia_rossii	PRJEB59163
Nyctibius_grandis	PRJNA562227
Nycticebus_coucang	PRJNA915385
Ochotona_princeps	PRJNA988022
Odontesthes_bonariensis	PRJNA923338
Onychomys_torridus	PRJEB39771
Orcinus_orca	PRJEB51334
Ornithorhynchus_anatinus	PRJNA513296
Osmerus_eperlanus	PRJEB64080
Pangasianodon_hypophthalmus	PRJNA915404
Parambassis_ranga	PRJEB30286
Pelecanus_crispus	PRJNA986544
Periophthalmus_magnuspinnatus	PRJNA562229
Petromyzon_marinus	PRJNA562230
Phaethornis_superciliosus	PRJNA789234
Phalacrocorax_aristotelis	PRJEB57282
Phocoena_sinus	PRJNA560233
Phoenicopterus_ruber_ruber	PRJNA562231
Pholidichthys_leucotaenia	PRJNA776880
Pholis_gunnellus	PRJEB43809
Phoxinus_phoxinus	PRJEB59308
Phyllostomus_discolor	PRJNA521246
Pipistrellus_kuhlii	PRJNA674391
Pipistrellus_pipistrellus	PRJEB39566
Pipistrellus_pygmaeus	PRJEB61049
Platichthys_flesus	PRJEB59806
Pleuronectes_platessa	PRJEB56054
Pluvialis_apricaria	PRJNA717218
Podarcis_cretensis	PRJEB61854
Podarcis_raffonei	PRJNA914745
Podargus_strigoides	PRJNA926650
Pogoniulus_pusillus	PRJNA641122
Pollachius_pollachius	PRJEB60645
Porphyrio_hochstetteri	PRJNA776871
Pristis_pectinata	PRJNA562240
Protomyctophum_parallelum	PRJEB63436
Pseudophryne_corroboree	PRJNA928730
Psittacula_echo	PRJEB64768
Pterocles_gutturalis	PRJNA562241
Pungitius_pungitius	PRJEB59310
Pygocentrus_nattereri	PRJNA562242
Raja_brachyura	PRJEB61690
Rana_temporaria	PRJEB42239
Rattus_norvegicus	PRJNA662962
Rhea_pennata	PRJNA928731
Rhinatrema_bivittatum	PRJEB32113
Rhineura_floridana	PRJNA972733
Rhinolophus_ferrumequinum	PRJNA526698
Rhynochetos_jubatus	PRJNA922141
Rissa_tridactyla	PRJNA911786
Rousettus_aegyptiacus	PRJNA674394
Rutilus_rutilus	PRJEB61621
Salarias_fasciatus	PRJEB33185
Salminus_brasiliensis	PRJNA976265
Salmo_trutta	PRJEB33201
Scatophagus_argus	PRJNA776881
Sciurus_carolinensis	PRJEB35387
Sciurus_vulgaris	PRJEB35381
Scleropages_formosus	PRJEB31997
Scomber_japonicus	PRJNA914746
Scyliorhinus_canicula	PRJEB35946
Sebastes_umbrosus	PRJNA562243
Silurus_aristotelis	PRJEB55446
Solea_solea	PRJEB61337
Sorex_araneus	PRJNA922145
Sparus_aurata	PRJEB31904
Spea_bombifrons	PRJNA915367
Sphaeramia_orbicularis	PRJEB33178
Spheniscus_humboldti	PRJNA922133
Squalius_cephalus	PRJEB59952
Stenella_coeruleoalba	PRJEB60665
Sterna_hirundo	PRJNA560234
Streptopelia_turtur	PRJEB32727
Strigops_habroptila	PRJNA510145
Suncus_etruscus	PRJNA844068
Sylvia_atricapilla	PRJNA560235
Sylvia_borin	PRJNA562244
Syngnathus_acus	PRJEB32743
Tachyglossus_aculeatus	PRJNA607289
Taeniopygia_guttata	PRJNA510143
Taeniopygia_guttata	PRJNA533101
Takifugu_rubripes	PRJEB31991
Tamandua_tetradactyla	PRJNA848843
Tauraco_erythrolophus	PRJNA562246
Taurulus_bubalis	PRJEB45118
Tautogolabrus_adspersus	PRJNA776882
Telmatherina_bonti	PRJEB51033
Tetrao_urogallus	PRJEB57676
Thalassophryne_amazonica	PRJEB34607
Thamnophis_elegans	PRJNA562247
Theristicus_caerulescens	PRJNA776872
Thunnus_albacares	PRJEB45170
Thunnus_maccoyii	PRJEB45115
Toxotes_jaculatrix	PRJNA717219
Trachurus_trachurus	PRJEB42240
Trichomycterus_rosablanca	PRJNA971190
Trichosurus_vulpecula	PRJNA562248
Trogon_surrucura	PRJNA776873
Tursiops_truncatus	PRJNA562249
Vidua_chalybeata	PRJNA912708
Vipera_seoanei	PRJNA858072
Vipera_ursinii	PRJEB55895
Xenentodon_cancila	PRJNA562250
Zalophus_californianus	PRJNA561800
Zeus_faber	PRJEB63619'''

data_dict = {}
lines = data.strip().split('\n')

for line in lines:
    fields = line.split('\t')
    if len(fields) == 2:
        species_dict = fields[0]
        bioproject_id = fields[1]
        data_dict[species_dict] = bioproject_id

# First part of the XML doc 
# can we include a second email? 

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
            <Contact email="vgl.metadata@rockefeller.edu"> #ed
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
#biosamples should be associated with bioproject
#some of the individuals have more than one biosample
#the one to use is the one that says animal sample

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
                <SPUID spuid_namespace="VGL"></SPUID>
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
                <SPUID spuid_namespace="VGL"></SPUID>
            </Identifier>
        </AddFiles>
    </Action>
    
    '''

# function to fill the xml doc (single library_layout)
# Function to fill XML template and add to final XML content

def fill_xml(xml_string, n):

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
        'BioSample': 'SAM67890'
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
#        ref_id_element = root.find(f"./AddFiles/AttributeRefId[@name='{ref_id_name}']/RefId/PrimaryId")
#        ref_id_element.text = data[ref_id_name]

        identifier_element = root.find("./AddFiles/Identifier/SPUID")
        identifier_element.text = str(uuid.uuid4())  # Generates a random UUID

        bioproject_id = data_dict.get(species[n], '')  # Get bioprojectID from data_dict
        attr_ref_id_element = root.find("./AddFiles/AttributeRefId[@name='BioProject']/RefId/PrimaryId")
        attr_ref_id_element.text = bioproject_id


    # Convert the updated XML back to a string
    updated_xml_string = ET.tostring(root, encoding='unicode')

    return(updated_xml_string) #switch this to append to xml file

#fill_xml(xml_string, 1)

#function to fill xml (paired library_layout) 
def fill_xml_paired(xml_string_pair, n):

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
        'BioSample': 'SAM67890'
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
#        ref_id_element = root.find(f"./AddFiles/AttributeRefId[@name='{ref_id_name}']/RefId/PrimaryId")
#        ref_id_element.text = data[ref_id_name]

        identifier_element = root.find("./AddFiles/Identifier/SPUID")
        identifier_element.text = str(uuid.uuid4())  # Generates a random UUID

        bioproject_id = data_dict.get(species[n], '')  # Get bioprojectID from data_dict
        attr_ref_id_element = root.find("./AddFiles/AttributeRefId[@name='BioProject']/RefId/PrimaryId")
        attr_ref_id_element.text = bioproject_id

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
            xml_filled = fill_xml(xml_string, n)
        elif n + 1 < len(path_list) and library_layout_list[n] == "paired" and library_layout_list[n + 1] == "paired":
            xml_filled = fill_xml_paired(xml_string_pair, n)
        else:
            raise ValueError(f"Invalid layout configuration at index {n}: {library_layout_list[n:n+2]}")

        # Append the filled XML to the final XML content
        final_xml_content += "\n\t" + xml_filled

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