from ase.data import chemical_symbols
import os
import requests
# kjpaw, kjpaw
url0 = 'https://pseudopotentials.quantum-espresso.org/upf_files/'
pseudos = {}
pseudo_type = 'kjpaw'
functional = 'pbe'
version = '1.0.0'
folder = f"psl_{version}_{functional}_{pseudo_type}"
if not os.path.exists(folder):
    os.makedirs(folder)
for ele in chemical_symbols:
# for ele in ['H', 'Be', 'Ti']:
    # for label in ['pbe', 'pbe-n', 'pbe-spn', 'pbe-spfn', 'pbe-spdn']:
    for label in ['', '-n', '-spn', '-spfn', '-spdn']:
    # for label in ['pbe-spdn']:
        prefix = '{}.{}{}-kjpaw_psl.{}.UPF'.format(ele, functional, label, version)
        url = url0 + prefix
        response = requests.head(url)
        print('url: ', url)
        if response.status_code == 200:  # HTTP 200 means OK
            out = os.system('wget -N -P %s %s'% (folder, url))
            if out != 0:
                continue
            pseudos[ele] = prefix
            # print('out: ', out)
        else:
            print("File does not exist")
print(pseudos)

