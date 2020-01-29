import os


def cat_file(path):
    if(os.path.exists(path)):
        os.system('cat {}'.format(path))


# Distro Informantion
print("Distro Info\n")
os.system('cat /etc/*-release')
cat_file('/etc/lsb-release')    
cat_file('/etc/redhat-release') 


# Environment Variables
print("Environment Variables")
cat_file("/etc/profile")
cat_file("/etc/bashrc")
cat_file("~/.bash_profile")
cat_file("~/.bashrc")
cat_file("~/.bash_logout")
os.system("env")
os.system("set")


# Printer Info
print("Is there a printer?\n")
os.system('lpstat -a')


# What services are running? Which service has which user privilege?
print("What services are running? Which service has which user privilege?")
os.system("ps aux")
os.system("ps -ef")
os.system("top")
os.system("^C")
cat_file("/etc/services")


# Which service(s) are been running by root? Of these services, which are vulnerable - it's worth a double check!
print("Which service(s) are been running by root? Of these services, which are vulnerable - it's worth a double check!")
os.system("ps aux | grep root")
os.system("ps -ef | grep root")


# What applications are installed? What version are they? Are they currently running?
print("Which service(s) are been running by root? Of these services, which are vulnerable - it's worth a double check!")
os.system("ls -alh /usr/bin/")
os.system("ls -alh /sbin/")
os.system("dpkg -l")
os.system("rpm -qa")
os.system("ls -alh /var/cache/apt/archivesO")
os.system("ls -alh /var/cache/yum/")


# Any of the service(s) settings misconfigured? Are any (vulnerable) plugins attached?
print(" service(s) settings misconfigured? Are any (vulnerable) plugins attached?")
cat_file("/etc/syslog.conf")
cat_file("/etc/chttp.conf")
cat_file("/etc/lighttpd.conf")
cat_file("/etc/cups/cupsd.conf")
cat_file("/etc/inetd.conf")
cat_file("/etc/apache2/apache2.conf")
cat_file("/etc/my.conf")
cat_file("/etc/httpd/conf/httpd.conf")
cat_file("/opt/lampp/etc/httpd.conf")
os.system("ls -aRl /etc/ | awk '$1 ~ /^.*r.*/")


# What jobs are scheduled?
print("What jobs are scheduled?")
os.system("crontab -l")
os.system("ls -alh /var/spool/cron")
os.system("ls -al /etc/ | grep cron")
os.system("ls -al /etc/cron*")
cat_file("/etc/cron*")
cat_file("/etc/at.allow")
cat_file("/etc/at.deny")
cat_file("/etc/cron.allow")
cat_file("/etc/cron.deny")
cat_file("/etc/crontab")
cat_file("/etc/anacrontab")
cat_file("/var/spool/cron/crontabs/root")


# Any plain text usernames and/or passwords?
print("Any plain text usernames and/or passwords?")
os.system("grep -i user [filename]")
os.system("grep -i pass [filename]")
os.system("grep -C 5 'password' [filename]")
os.system("find . -name '*.php' -print0 | xargs -0 grep -i -n 'var $password'")


# Communications and Networking

# What NIC(s) does the system have? Is it connected to another network?
print("What NIC(s) does the system have? Is it connected to another network?")
os.system("/sbin/ifconfig -a")
cat_file("/etc/network/interfaces")
cat_file("/etc/sysconfig/network")


# What are the network configuration settings? What can you find out about this network? DHCP server? DNS server? Gateway?
print("What are the network configuration settings? What can you find out about this network? DHCP server? DNS server? Gateway?")
cat_file("/etc/resolv.conf")
cat_file("/etc/sysconfig/network")
cat_file("/etc/networks")
os.system("iptables -L")
os.system("hostname")
os.system("dnsdomainname")


# What other users & hosts are communicating with the system?
print("What other users & hosts are communicating with the system?")
os.system("lsof -i")
os.system("lsof -i :80")
os.system("grep 80 /etc/services")
os.system("netstat -antup")
os.system("netstat -antpx")
os.system("netstat -tulpn")
os.system("chkconfig --list")
os.system("chkconfig --list | grep 3:on")
os.system("last")
os.system("w")


# Whats cached? IP and/or MAC addresses
print("Whats cached? IP and/or MAC addresses")
os.system("arp -e")
os.system("route")
os.system("/sbin/route -nee")

# Confidential Information & Users
print("Confidential Information & Users")
os.system("id")
os.system("who")
os.system("w")
os.system("last")
cat_file("/etc/passwd | cut -d: -f1    # List of users")
os.system("grep -v -E '^#' /etc/passwd | awk -F: '$3 == 0 { print $1}'")   # List of super users
print("List of Super Users")
os.system("awk -F: '($3 == '0') {print}' /etc/passwd")
os.system("cat /etc/sudoers")
os.system("sudo -l")


# What sensitive files can be found?
print("What sensitive files can be found?")
cat_file("/etc/passwd")
cat_file("/etc/group")
cat_file("/etc/shadow")
os.system("ls -alh /var/mail/")


# Anything "interesting" in the home directorie(s)? If it's possible to access
print("Anything 'interesting' in the home directorie(s)? If it's possible to access")
os.system("ls -ahlR /root/")
os.system("ls -ahlR /home/")


# Are there any passwords in; scripts, databases, configuration files or log files? Default paths and locations for passwords
print("Are there any passwords in; scripts, databases, configuration files or log files? Default paths and locations for passwords")
cat_file("/var/apache2/config.inc")
cat_file("/var/lib/mysql/mysql/user.MYD")
cat_file("/root/anaconda-ks.cfg")


# What has the user being doing? Is there any password in plain text? What have they been edting?
print("What has the user being doing? Is there any password in plain text? What have they been edting?")
cat_file("~/.bash_history")
cat_file("~/.nano_history")
cat_file("~/.atftp_history")
cat_file("~/.mysql_history")
cat_file("~/.php_history")


# What user information can be found?
print("What user information can be found?")
cat_file("~/.bashrc")
cat_file("~/.profile")
cat_file("/var/mail/root")
cat_file("/var/spool/mail/root")


# Can private-key information be found?
print("Can private-key information be found?")
cat_file("~/.ssh/authorized_keys")
cat_file("~/.ssh/identity.pub")
cat_file("~/.ssh/identity")
cat_file("~/.ssh/id_rsa.pub")
cat_file("~/.ssh/id_rsa")
cat_file("~/.ssh/id_dsa.pub")
cat_file("~/.ssh/id_dsa")
cat_file("/etc/ssh/ssh_config")
cat_file("/etc/ssh/sshd_config")
cat_file("/etc/ssh/ssh_host_dsa_key.pub")
cat_file("/etc/ssh/ssh_host_dsa_key")
cat_file("/etc/ssh/ssh_host_rsa_key.pub")
cat_file("/etc/ssh/ssh_host_rsa_key")
cat_file("/etc/ssh/ssh_host_key.pub")
cat_file("/etc/ssh/ssh_host_key")


# File Systems

# Which configuration files can be written in /etc/? Able to reconfigure a service?
print("Which configuration files can be written in /etc/? Able to reconfigure a service?")
os.system("ls -aRl /etc/ | awk '$1 ~ /^.*w.*/' 2>/dev/null     # Anyone")
os.system("ls -aRl /etc/ | awk '$1 ~ /^..w/' 2>/dev/null       # Owner")
os.system("ls -aRl /etc/ | awk '$1 ~ /^.....w/' 2>/dev/null    # Group")
os.system("ls -aRl /etc/ | awk '$1 ~ /w.$/' 2>/dev/null        # Other")
os.system("find /etc/ -readable -type f 2>/dev/null               # Anyone")
os.system("find /etc/ -readable -type f -maxdepth 1 2>/dev/null   # Anyone")


# What can be found in /var/ ?
print("What can be found in /var/ ?")
os.system("ls -alh /var/log")
os.system("ls -alh /var/mail")
os.system("ls -alh /var/spool")
os.system("ls -alh /var/spool/lpd")
os.system("ls -alh /var/lib/pgsql")
os.system("ls -alh /var/lib/mysql")
cat_file("/var/lib/dhcp3/dhclient.leases")


# Any settings/files (hidden) on website? Any settings file with database information?
print("Any settings/files (hidden) on website? Any settings file with database information?")
os.system("ls -alhR /var/www/")
os.system("ls -alhR /srv/www/htdocs/")
os.system("ls -alhR /usr/local/www/apache22/data/")
os.system("ls -alhR /opt/lampp/htdocs/")
os.system("ls -alhR /var/www/html/")


# Is there anything in the log file(s) (Could help with "Local File Includes"!)
print("Is there anything in the log file(s) (Could help with 'Local File Includes'!")
cat_file("/etc/httpd/logs/access_log")
cat_file("/etc/httpd/logs/access.log")
cat_file("/etc/httpd/logs/error_log")
cat_file("/etc/httpd/logs/error.log")
cat_file("/var/log/apache2/access_log")
cat_file("/var/log/apache2/access.log")
cat_file("/var/log/apache2/error_log")
cat_file("/var/log/apache2/error.log")
cat_file("/var/log/apache/access_log")
cat_file("/var/log/apache/access.log")
cat_file("/var/log/auth.log")
cat_file("/var/log/chttp.log")
cat_file("/var/log/cups/error_log")
cat_file("/var/log/dpkg.log")
cat_file("/var/log/faillog")
cat_file("/var/log/httpd/access_log")
cat_file("/var/log/httpd/access.log")
cat_file("/var/log/httpd/error_log")
cat_file("/var/log/httpd/error.log")
cat_file("/var/log/lastlog")
cat_file("/var/log/lighttpd/access.log")
cat_file("/var/log/lighttpd/error.log")
cat_file("/var/log/lighttpd/lighttpd.access.log")
cat_file("/var/log/lighttpd/lighttpd.error.log")
cat_file("/var/log/messages")
cat_file("/var/log/secure")
cat_file("/var/log/syslog")
cat_file("/var/log/wtmp")
cat_file("/var/log/xferlog")
cat_file("/var/log/yum.log")
cat_file("/var/run/utmp")
cat_file("/var/webmin/miniserv.log")
cat_file("/var/www/logs/access_log")
cat_file("/var/www/logs/access.log")
os.system("ls -alh /var/lib/dhcp3/")
os.system("ls -alh /var/log/postgresql/")
os.system("ls -alh /var/log/proftpd/")
os.system("ls -alh /var/log/samba/")


# Note: auth.log, boot, btmp, daemon.log, debug, dmesg, kern.log, mail.info, mail.log, mail.warn, messages, syslog, udev, wtmp

# How are file-systems mounted?
print("How are file-systems mounted?")
os.system("mount")
os.system("df -h")


# Are there any unmounted file-systems?
print("Are there any unmounted file-systems?")
cat_file("/etc/fstab")


# What "Advanced Linux File Permissions" are used? Sticky bits, SUID & GUID
print("What Advanced Linux File Permissions are used? Sticky bits, SUID & GUID")
os.system("find / -perm -1000 -type d 2>/dev/null   # Sticky bit - Only the owner of the directory or the owner of a file can delete or rename here.")
os.system("find / -perm -g=s -type f 2>/dev/null    # SGID (chmod 2000) - run as the group, not the user who started it.")
os.system("find / -perm -u=s -type f 2>/dev/null    # SUID (chmod 4000) - run as the owner, not the user who started it.")
os.system("find / -perm -g=s -o -perm -u=s -type f 2>/dev/null    # SGID or SUID")
# Looks in 'common' places: /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, /usr/local/sbin and any other *bin, for SGID or SUID (Quicker search)
os.system("for i in `locate -r 'bin$'`; do find $i \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null; done")    


# find starting at root (/), SGID or SUID, not Symbolic links, only 3 folders deep, list with more detail and hide any errors (e.g. permission denied)
os.system("find / -perm -g=s -o -perm -4000 ! -type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null")


# Where can written to and executed from? A few 'common' places: /tmp, /var/tmp, /dev/shm
print("Where can written to and executed from? A few 'common' places: /tmp, /var/tmp, /dev/shm")
os.system("find / -writable -type d 2>/dev/null      # world-writeable folders")
os.system("find / -perm -222 -type d 2>/dev/null     # world-writeable folders")
os.system("find / -perm -o w -type d 2>/dev/null     # world-writeable folders")
os.system("find / -perm -o x -type d 2>/dev/null     # world-executable folders")
os.system("find / \( -perm -o w -perm -o x \) -type d 2>/dev/null   # world-writeable & executable folders")


# Any "problem" files? Word-writeable, "nobody" files
print("Any 'problem' files? Word-writeable, 'nobody' files")
os.system("find / -xdev -type d \( -perm -0002 -a ! -perm -1000 \) -print   # world-writeable files")
os.system("find /dir -xdev \( -nouser -o -nogroup \) -print   # Noowner files")


# Preparation & Finding Exploit Code

# What development tools/languages are installed/supported?
print("What development tools/languages are installed/supported?")
os.system("find / -name perl*")
os.system("find / -name python*")
os.system("find / -name gcc*")
os.system("find / -name cc")


# How can files be uploaded?
print("How can files be uploaded?")
os.system("find / -name wget")
os.system("find / -name nc*")
os.system("find / -name netcat*")
os.system("find / -name tftp*")
os.system("find / -name ftp")
