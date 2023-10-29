from ehpc_colors import eColors

# DEBUG CODE
debug = 1
if debug:
    dc = '002: '
else:
    dc =''

class LoginNode:
    """EHPC class that defines Login Nodes"""
    def __init__(self, name, ip):
        self.name    = name
        self.ip      = ip
        self.idm     = 'local'  # Choose AD,LDAP,sssd, etc.
        self.storage = 'local'
        # I expect this to be set at the cluster level in the future.
        # For now it'll be split from the fqdn
        self.domain  = 'ehpc.org' 

        ename = self.name.split('.')
        ename.pop(0)
        self.domain = '.'.join(ename)

    def __repr__(self):
        return "Login()"
    def __str__(self):
        login_print = f"LoginNode name: {self.name}, ip: {self.ip}, idm: {self.idm}, storage: {self.storage}, domain: {self.domain}"
        return login_print
    def getName(self):
        return self.name

    def validateNode(self):
        #TODO:
        # Check DNS (For simple forward DNS lookups, it's better to use socket.getaddrinfo() or socket.gethostbyname().)
        # Ping IP
        # Login with SSH (First check for saved SSH Key for eHPC)
        # Optional (doens't cause a failed test) Run sinfo and other scheduler equivalent
        pass
