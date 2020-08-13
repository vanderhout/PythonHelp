import os
from PlannerComponent.Common import file_list_from_path

venv_scripts_path = r'C:\Users\russe\Desktop\Planner\Repository\PlannerAdmin\planneradmin\venv\Scripts'
input_path = r'C:\Users\russe\Desktop\Planner\Repository\PlannerAdmin\planneradmin\Run'
output_path = r'C:\Users\russe\Desktop\PlannerAdminShortcuts'

subpaths = file_list_from_path(input_path, True)

for subpath in subpaths:
    basename = os.path.basename(subpath)
    if basename == 'main.py':
        [output_file_path, _] = os.path.splitext(os.path.join(output_path, subpath))
        output_file_path += '.bat'

        output_file_dir = os.path.dirname(output_file_path)

        latest_existing_ancestor = output_file_dir
        to_create = []
        while not os.path.exists(latest_existing_ancestor):
            to_create.append(latest_existing_ancestor)
            latest_existing_ancestor = os.path.dirname(latest_existing_ancestor)
        while to_create:
            os.mkdir(to_create[-1])
            to_create.pop(-1)

        file = open(output_file_path, 'w')

        full_path = os.path.join(input_path, subpath)
        cmd = 'cmd /k "cd /d "{}" & activate & cd /d "{}" & python {}"'.format(venv_scripts_path, os.path.dirname(full_path), basename)
        file.write(cmd)

        file.close()