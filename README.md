#Preparation
Make sure you have the following installed:
* Python 2.7.x
* MongoDB	2.6.x

Pull this down:
```
git clone https://github.com/ckane/revolutionuc-cybersecurity.git
```

#Install CRITs

CRITs Documentation:
* https://github.com/crits/crits/wiki

On Ubuntu:
```
apt-get install mongodb-server zip p7zip-full p7zip-rar libjpeg-dev
apt-get install build-essential curl git libevent-dev libz-dev libjpeg-dev
apt-get install libfuzzy-dev libldap2-dev libpcap-dev libpcre3-dev
apt-get install libsasl2-dev libxml2-dev libxslt1-dev libyaml-dev numactl
apt-get install p7zip-full python-dev python-pip ssdeep upx zip swig
apt-get install libssl-dev
pip install virtualenv virtualenv-clone virtualenvwrapper yara-python
pip install libtaxii stix
```

Make a CRITs-specific virtualenv:
```
mkvirtualenv crits
mkdir ~/src/crits
cd ~/src/crits
pip install -U -r requirements.txt
```

Create a data folder for db and logs, owner should be crits user:
```
mkdir -p /data/db /data/logs
chown -R ckane /data
```

Initialize database environments with CRITs data, and add admin user:
```
bash script/bootstrap 4
```

Pull down services:
```
cd /data
git clone https://github.com/crits/crits_services.git
cd ~/src/crits
cat /data/crits_services/*/requirements.txt | sort | uniq > services-req.txt
pip install -U -r services-req.txt
pip install pytx stix-ramrod passivetotal numpy stix-validator
```

Start CRITS:
```
cd ~/src/crits
bash ./script/server
```

In the CRITs Control Panel, you'll want to do the following:
* Enable API
* Add source names for sources you'll get intelligence from
* Add these sources to the user you are logging in as
* Set the path for CRITs services (and restart CRITs)

#Install Maltrieve
```
workon crits
git clone https://github.com/krmaxwell/maltrieve.git
pip install feedparser grequests bs4 python-magic requests
```
#Sources for Intelligence
(some assembly required)

The following are decent places to find intelligence that could be imported into CRITs:
* http://malc0de.com/database/
* https://otx.alienvault.com/
* https://intel.criticalstack.com/
* https://www.virustotal.com/en/documentation/public-api/
