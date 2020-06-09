import os
import argparse
import re
import time
import subprocess
import configparser

class Plink_GWAS():
    """Create a class to create an object for the Plink GWAS command
    Parameters:
        A class name for initiation call
    Output:
        An object of class Plink_GWAS
    And so on...
    """
    def __init__(self, class_name):
        self.class_name=class_name
        self.cmd_path=''
        self.bfile=''
        self.regression_model=''
        self.ci=''
        self.covar_file_name=''
        self.covar_list=[]#this a list
        self.output_file_name=''
        self.hide_covar=''
        self.pheno_file=''
        self.pheno_name=''

    def init_param_configparser(self, conf_file):
        config = configparser.ConfigParser()
        config.read(conf_file)
        #print(config.sections())
        #set the object parameters
        self.cmd_path=config['plink_gwas']['cmd_path']
        #print('cmd_path:', self.cmd_path)
        self.bfile=config['plink_gwas']['bfile']
        self.regression_model=config['plink_gwas']['regression_model']
        self.ci=config['plink_gwas']['ci']
        self.covar_file_name=config['plink_gwas']['covar_file_name']
        self.output_file_name=config['plink_gwas']['output_file_name']
        self.hide_covar=config['plink_gwas']['hide_covar']
        if(self.hide_covar == 'yes'):
            self.hide_covar= ' --hide-covar '
        else:
            self.hide_covar= ' '
        #read the covars and store as a list
        #tmpCovar=config['plink_gwas']['covar_list']
        #tmpCovar=tmpCovar.split(',')
        #tmpCovar = [x.strip(' ') for x in tmpCovar]
        #self.covar_list=tmpCovar
        self.covar_list=config['plink_gwas']['covar_list']
        #print('list:', self.covar_list)
        self.pheno_file=config['plink_gwas']['pheno_file']
        self.pheno_name=config['plink_gwas']['pheno_name']
        self.allow_no_sex=config['plink_gwas']['allow-no-sex']
        if(self.allow_no_sex == 'yes'):
            self.allow_no_sex= ' --allow-no-sex '
        else:
            self.hide_covar= ' '


    def init_param_user():
        pass

    def call_plink_gwas(self):
        #prepare the command
        print('f:', self.output_file_name)
        cmd = self.cmd_path + 'plink --bfile ' +  self.bfile + ' ' + \
        ' --' + self.regression_model + ' --ci ' + self.ci + ' ' + self.hide_covar + \
        ' --covar ' + self.covar_file_name + ' --covar-name ' + self.covar_list + \
        ' --pheno ' + self.pheno_file + ' --pheno-name ' + self.pheno_name + \
        self.allow_no_sex + \
        ' --out ' + self.output_file_name

        print('plink gwas cmd:', cmd)
        #call the cmd
        subprocess.run(cmd, shell=True)

    def print_plink_cmd(self):
        print('plink cmd path:',self.cmd_path )

    def print_class_name(self):
        """Print the class name
        Parameters:
            no parmaeters
        """
        print('The class name is:',self.class_name)


def main():
    #example of running the script is:
    #python call_plink_gwas.py -conf_file plink_gwas_config_1.txt
    #python call_plink_gwas.py -conf_file demo_config_1.txt
    parser = argparse.ArgumentParser()
    parser.add_argument("-conf_file", "--conf_file",  help="Proivde configuration file")
    args = parser.parse_args()
    print('Function to call Plink GWAS')
    print('config file is:', args.conf_file)

    # initiate the class object
    class_name='Plink-GWAS'
    plink_obj=Plink_GWAS(class_name)

    #call a function from the class
    plink_obj.print_class_name()


    #set the parameters using the config file
    plink_obj.init_param_configparser(args.conf_file)


    #call the plink gwas command
    plink_obj.call_plink_gwas()

    #print plink cmd path
    #plink_obj.print_plink_cmd()

main()
