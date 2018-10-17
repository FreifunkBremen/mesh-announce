import providers
from providers.babel import dump as babeldump

class Source(providers.DataSource):
    def required_args(self):
        return ['babel_addr']

    def call(self, babel_addr):
        if babel_addr is None:
            return None
        ret = {}
        result = babeldump(babel_addr)
        for dataIF in result:
            if dataIF[0] == "add" and dataIF[1] == "interface" and dataIF[4] == "true" and dataIF[5] == "ipv6":
        	       ret[dataIF[2]] = {
        		         "ll-addr": dataIF[6],
    		               "protocol": "babel",
                           "neighbours": ( lambda result, ifname: {
                            data[4]: {
                                "rxcost": int(data[12]),
                                "txcost": int(data[14]),
                                "cost": int(data[16]),
                                "reachability": int(data[8],16)
                            }
                            for data in result
                            if data[0] == "add" and data[1] == "neighbour" and data[3] == "address" and data[5] == "if" and data[6] == ifname and data[7] == "reach" and data[11] == "rxcost" and data[13] == "txcost" and data[15] == "cost"
                            })(result,dataIF[2])
                        }
        return ret
