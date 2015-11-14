#!/usr/bin/python
import Queue
import sys #for command line args
import math
import numpy as np
from lib_matt import printV


class rejection_sampling():
    def __init__(self):
        self.samples = np.array([0.82, 0.56, 0.08, 0.81, 0.34, 0.22, 0.37, 0.99,
                                 0.55, 0.61, 0.31, 0.66, 0.28, 1.00, 0.95, 0.71,
                                 0.14, 0.10, 1.00, 0.71, 0.10, 0.60, 0.64, 0.73,
                                 0.39, 0.03, 0.99, 1.00, 0.97, 0.54, 0.80, 0.97,
                                 0.07, 0.69, 0.43, 0.29, 0.61, 0.03, 0.13, 0.14,
                                 0.13, 0.40, 0.94, 0.19, 0.60, 0.68, 0.36, 0.67,
                                 0.12, 0.38, 0.42, 0.81, 0.00, 0.20, 0.85, 0.01,
                                 0.55, 0.30, 0.30, 0.11, 0.83, 0.96, 0.41, 0.65,
                                 0.29, 0.40, 0.54, 0.23, 0.74, 0.65, 0.38, 0.41,
                                 0.82, 0.08, 0.39, 0.97, 0.95, 0.01, 0.62, 0.32,
                                 0.56, 0.68, 0.32, 0.27, 0.77, 0.74, 0.79, 0.11,
                                 0.29, 0.69, 0.99, 0.79, 0.21, 0.20, 0.43, 0.81,
                                 0.90,  0.00,  0.91,  0.01]);
        printV(["samples: ",self.samples],1);
        self.cpt = {"cloudy":[0.5],"sprinkler":[0.1,0.5],"rain":[0.8,0.2],"wet":[0.99,0.90,0.90,0.00]}
        self.valid_array = [];
        self.sample_cnt = 0;


    def get_sample(self):
        self.sample_cnt = self.sample_cnt +1;
        return self.samples[self.sample_cnt - 1];


    # if check is greater than mark return false
    def check_mark(self,check,mark):
        printV(["check",check],1);
        printV(["mark",mark],1);
        if (check <= mark):
            return True;
        else: return False;
    # ...

    # return None if cloudy given contradicts the sample
    # else return True/False
    def add_temp_sample(self,sample,given_dict,name,cpt_val):
        printV(["sample: ",sample,"given_dict: ",given_dict],1);
        printV(['self.cpt[name][cpt_val]',self.cpt[name][cpt_val]],1);
        name_val = self.check_mark(sample,self.cpt[name][cpt_val]);
        if (name in given_dict)is True:
            #  cloudy is in given
            if (given_dict[name] == name_val)is True:
                # no contradition
                return name_val;
            else:
                # cloudy is given and sample contradicts
                return None;
        else:
            # cloudy is not in given
            return name_val


    #  Return true to start a new iteration
    #  Return false to print valid
    def set_sample_dict(self,given_dict):
        #  This is where you will call each node
        #  Each node will return true to keep going
        #  will return false to start a new iteration
        temp_dict = {};
        #cloudy
        if (self.sample_cnt < len(self.samples)) is True:
            cloudy_sample = self.get_sample();
            printV(["cloudy sample: ",cloudy_sample],1);
            cloudy_ret = self.add_temp_sample(cloudy_sample,given_dict,'cloudy',0);
            #  if false start a new iteration
            if (cloudy_ret == None)is True: return True;
            else: temp_dict['cloudy'] = cloudy_ret;
        else:  return False;
        printV(["temp_dict after cloudy check",temp_dict],1);

        # sprinkler
        # set cpt_val for sprinkler based on cloudy_val
        if (temp_dict['cloudy'] == False)is True: cpt_s = 1;
        else: cpt_s = 0;

        if (self.sample_cnt < len(self.samples)) is True:
            sprinkler_sample = self.get_sample();
            printV(["sprinkler sample: ",sprinkler_sample],1);
            sprinkler_ret = self.add_temp_sample(sprinkler_sample,given_dict,'sprinkler',cpt_s);
            #  if false start a new iteration
            if (sprinkler_ret == None)is True: return True;
            else: temp_dict['sprinkler'] = sprinkler_ret;
        else:  return False;
        printV(["temp_dict after sprinkler check",temp_dict],1);

        # rain
        # set cpt_val for rain based on cloudy_val
        if (self.sample_cnt < len(self.samples)) is True:
            rain_sample = self.get_sample();
            printV(["rain sample: ",rain_sample],1);
            rain_ret = self.add_temp_sample(rain_sample,given_dict,'rain',cpt_s);
            #  if false start a new iteration
            if (rain_ret == None)is True: return True;
            else: temp_dict['rain'] = rain_ret;
        else:  return False;
        printV(["temp_dict after rain check",temp_dict],1);

        # wet
        # set cpt_val for wet based on sprinkler_val and rain_val
        if    ((temp_dict['sprinkler'] == True)  is True and
              (temp_dict['rain'] == True)        is True): cpt_w = 0;
        elif  ((temp_dict['sprinkler'] == True)  is True and
              (temp_dict['rain'] == False)       is True): cpt_w = 1;
        elif  ((temp_dict['sprinkler'] == False) is True and
              (temp_dict['rain'] == True)        is True): cpt_w = 2;
        elif  ((temp_dict['sprinkler'] == False) is True and
              (temp_dict['rain'] == False)       is True): cpt_w = 3;
        printV(["cpt_w value:",cpt_w],1);


        if (self.sample_cnt < len(self.samples)) is True:
            wet_sample = self.get_sample();
            printV(["wet sample: ",wet_sample],1);
            wet_ret = self.add_temp_sample(wet_sample,given_dict,'wet',cpt_w);
            #  if false start a new iteration
            if (wet_ret == None)is True: return True;
            else: temp_dict['wet'] = wet_ret;
        else:  return False;
        printV(["temp_dict after wet check",temp_dict],1);

        printV("----- Iteration satisfies all given values -----",1);
        self.valid_array.append(temp_dict);
        return True;






    def make_valid_array(self,given_dict):
        return_val=1;
        while(return_val):
            printV("********************************************",1);
            return_val = self.set_sample_dict(given_dict)
            printV(self.valid_array,1);
        for i in range(len(self.valid_array)):
            printV([i,': ',self.valid_array[i]],1);


    def rejection_prob(self,name,given_dict):
        self.make_valid_array(given_dict);
        true_cnt = 0;
        false_cnt = 0;
        for valid_it in self.valid_array:
            if (valid_it[name] == True)is True:
                true_cnt = true_cnt + 1;
            else:
                false_cnt = false_cnt + 1;
        return np.array([float(true_cnt)/len(self.valid_array),float(false_cnt)/len(self.valid_array)]);


def main():
    rs = rejection_sampling();
    printV("Problem 2: Rejection sampling",2);

    return_val = rs.rejection_prob('cloudy',{});
    printV(["a.  P(c = True): ",return_val[0]],2);
    rs.sample_cnt = 0;
    rs.valid_array=[];

    return_val = rs.rejection_prob('cloudy',{'rain':True});
    printV(["b.  P(c = True | rain = True): ",return_val[0]],2);
    rs.sample_cnt = 0;
    rs.valid_array=[];

    return_val = rs.rejection_prob('sprinkler',{'wet':True});
    printV(["c.  P(s = True | wet = True): ",return_val[0]],2);
    rs.sample_cnt = 0;
    rs.valid_array=[];

    return_val = rs.rejection_prob('sprinkler',{'wet':True,'cloudy':True});
    printV(["d.  P(s = True | wet = True, cloudy = True): ",return_val[0]],2);
    rs.sample_cnt = 0;
    rs.valid_array=[];

if __name__ == "__main__":
    main()
