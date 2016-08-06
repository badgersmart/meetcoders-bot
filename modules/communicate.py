import requests
import ConfigParser, os

class Communicate(object):
    """docstring for """
    def __init__(self,configfile):
        self.load_config(configfile)
        self.token   = self.config.get('ACCOUNT','TOKEN')
        self.version = self.config.get('ACCOUNT','VERSION')
        self.host    = self.config.get('ACCOUNT','HOST')
        self.namebot    = self.config.get('ACCOUNT','NAMEBOT')
        self.nameproject = self.config.get('ACCOUNT','NAMEPROJECT')
        self.get_id_project()
        self.get_labels()


    def get_id_project(self):
        for project in self.get_data('projects'):
            if project["name"] == self.nameproject:
                self.id_project = project['id']
                break;
    def get_labels(self):
        self.labels = []
        for label in self.get_data('/projects/'+str(self.id_project)+'/labels'):
            self.labels.append(label['name'])
    def get_data(self,url):
        r = requests.get(self.host+'api/v'+str(self.version)+'/'+url+'?private_token='+self.token)
        return r.json()
    def delete_data(self,url):
        r = requests.delete(self.host+'api/v'+str(self.version)+'/'+url+'?private_token='+self.token)
        return r.json()
    def put_data(self,url,data):
        r = requests.put(self.host+'api/v'+str(self.version)+'/'+url+'?private_token='+self.token,data)
        return r.json()
    def post_data(self,url,data):
        r = requests.post(self.host+'api/v'+str(self.version)+'/'+url+'?private_token='+self.token,data)
        return r.json()

    def get_all_merge_requests(self):
        return self.get_data('/projects/'+str(self.id_project)+'/merge_requests')

    def get_merge_request(self,id):
        return self.get_data('/projects/'+str(self.id_project)+'/merge_requests/'+str(id))

    def get_notes_of_mr(self,id):
        return self.get_data('/projects/'+str(self.id_project)+'/merge_requests/'+str(id)+'/notes')

    def work_labels(self):
        for mr in self.get_all_merge_requests():
            self.mr_labels = mr['labels']
            for note in self.get_notes_of_mr(str(mr['id'])):
                if "@"+self.namebot in note['body']:
                    self.check_label_and_action(mr['id'],note)
                else:
                    continue;
    def update_mr_with_label(self,mr_id,label,add):
        if add and label not in self.mr_labels:
            self.mr_labels.append(label)
        elif not add:
            self.mr_labels.remove(label)
        self.put_data('/projects/'+str(self.id_project)+'/merge_requests/'+str(mr_id),{"labels" : ','.join(self.mr_labels)})
    def check_label_and_action(self,mr_id,note):
        add = False
        if "@"+self.namebot+" add_label" in note['body']:
            labs = note['body'].split("add_label")[1].split(", ")
            add = True
        elif "@"+self.namebot+" remove_label" in note['body']:
            labs = note['body'].split("remove_label")[1].split(", ")
        else:
            #create note
            return 0
        for lab in labs:
            lab_target = lab.replace(' ','')
            if self.check_label(lab_target):
                self.update_mr_with_label(mr_id,lab_target,add)
                #self.delete_data('/projects/'+str(self.id_project)+'/merge_requests/'+str(mr_id)+'/notes/'+str(note['id']))
            else:
                return 0
        #self.delete_data('/projects/'+str(self.id_project)+'/merge_requests/'+str(mr_id)+'/notes/'+str(note['id']))
    def check_label(self,label):
        return label in self.labels
    def look_for_rubocop(self,notes):
            return 1
    def launch_rubocop(self):
            print('Rubocop')
    def work_rubocop(self):
        for mr in self.get_all_merge_requests():
            print(mr)
            if self.look_for_rubocop():
                print("Yeu")
                print(self.host+"le.com/api/v3/projects/"+mr["source_project_id"]+"/repository/branches")
            else:
                launch_rubocop()
            for commit in self.get_data('/projects/'+str(self.id_project)+'/merge_requests/'+str(mr['id'])+'/commits'):
                print(commit)
