# coding=utf-8
from __future__ import unicode_literals
import paramiko
import hashlib


class Ssh(object):

    def __init__(self, hostname="127.0.0.1", username="root", password=None, port=22, key_file=None, key_password=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = int(port)
        self.key_file = key_file
        self.key_pw = key_password
        self.PROFILE = ". /etc/profile 2&>/dev/null;. ~/.bash_profile 2&>/dev/null;. /etc/bashrc 2&>/dev/null;"
        self.PATH = "export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin;"
        self.ssh = self.ssh_conn()
        self._sftp_conn, self.sftp = self.sftp_conn()

    def _pkey(self):
        if self.key_pw:
            pkey = paramiko.RSAKey.from_private_key_file(self.key_file, password=self.key_pw)
        else:
            pkey = paramiko.RSAKey.from_private_key_file(self.key_file)
        return pkey

    def cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(self.PROFILE+self.PATH+cmd)

        result = stdout.read(), stderr.read()
        if any(result):
            cmd_result = filter(lambda x:len(x.strip())>0,result)[0]
        else:
            cmd_result = 'execution has no output!'
        return cmd_result

    def ssh_conn(self):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pkey = self._pkey()
        try:
            s.connect(hostname=self.hostname, port=self.port, username=self.username, pkey=pkey)
        except:
            raise
        return s

    def sftp_conn(self):
        s = paramiko.Transport((self.hostname, self.port))
        s.connect(username=self.username,pkey=self._pkey())
        sftp = paramiko.SFTPClient.from_transport(s)
        return s, sftp

    def close(self):
        self.ssh.close()
        self.sftp.close()
        self._sftp_conn.close()

# s = SshPro(hostname="s2.95xd.com",username="root",key_file="/Users/xieyixue/.ssh/id_rsa")
# print s.ftp("/installer.failurerequests","/tmp/1111")


class SshStore(object):
    """
    存储所有ssh对象, 统一维护ssh连接
    """

    def __init__(self):
        self.store = {}

    def create(self, host):
        """
        传入主机对象, 创建连接并推送到管理仓库
        """
        md5 = self.hash_host(host)
        ssh = Ssh(**host)
        self.store[md5] = ssh
        return ssh

    def get(self, host):
        md5 = self.hash_host(host)
        ssh = self.store.get(md5)
        return ssh

    def delete(self, host):
        md5 = self.hash_host(host)
        if md5 in self.store:
            conn = self.store.pop(md5, None)
            conn.close()
        return True

    @staticmethod
    def hash_host(host):
        return hashlib.md5.update(host).hexdigest()

