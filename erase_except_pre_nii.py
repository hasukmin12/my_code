import os
import shutil

path = '/home/has/Datasets/(has)CT_nii'
case_list = next(os.walk(path))[1]
case_list.sort()
print(case_list)

output_path = '/home/has/Datasets/(has)CT_nii6'
if os.path.isdir(output_path)==False:
    os.makedirs(output_path)

for case in case_list:
    in_case = os.path.join(path,case)
    file_list = next(os.walk(in_case))[2]
    file_list.sort()
    print(file_list)

    folder_name = "case_{0:05d}".format(case_list.index(case))
    folder_path = os.path.join(output_path,folder_name)
    if os.path.isdir(folder_path)==False:
        os.makedirs(folder_path)


    for list in file_list:
        if 'pre' in list:
            print(list)
            print("")
            output_name = os.path.join(folder_path,'imaging.nii.gz')
            shutil.copyfile(os.path.join(in_case,list),os.path.join(output_path,output_name))

        elif list == '2_.nii.gz':
            print(list)
            print("")
            output_name = os.path.join(folder_path, 'imaging.nii.gz')
            shutil.copyfile(os.path.join(in_case, list), os.path.join(output_path, output_name))

        elif '201_' in list:
            print(list)
            print("")
            output_name = os.path.join(folder_path,'imaging.nii.gz')
            shutil.copyfile(os.path.join(in_case,list),os.path.join(output_path,output_name))

        elif '203_' in list:
            print(list)
            print("")
            output_name = os.path.join(folder_path, 'imaging.nii.gz')
            shutil.copyfile(os.path.join(in_case, list), os.path.join(output_path, output_name))

        elif list == '3_.nii.gz':
            print(list)
            print("")
            output_name = os.path.join(folder_path, 'imaging.nii.gz')
            shutil.copyfile(os.path.join(in_case, list), os.path.join(output_path, output_name))

        elif list == 'imaging.nii.gz':
            print(list)
            print("")
            output_name = os.path.join(folder_path, 'imaging.nii.gz')
            shutil.copyfile(os.path.join(in_case, list), os.path.join(output_path, output_name))