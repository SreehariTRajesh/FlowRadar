def ip_to_integer(ip_addr: str):
    num_list: list[int] = [ int(x) for x in ip_addr.split(".") ]
    convertedIP: int = 0
    factor: int = 1
    for num in num_list:
        convertedIP += factor * num
        factor *= 256
    return convertedIP
        
def hash1(flow: tuple[str, str, int, int, int], filter_size: int):
    src_ip: str
    dest_ip: str
    src_port: int
    dest_port: int
    protocol: int 
    src_ip, dest_ip, src_port, dest_port, protocol = flow
    src_ip = ip_to_integer(src_ip)
    dest_ip = ip_to_integer(dest_ip)
    HX = src_ip * 59 ^ dest_ip * 59 ^ src_port * 59 ^ dest_port * 59 ^ protocol * 59
    return HX    

def hash2(flow: tuple[str, str, int, int, int], filter_size: int):
    src_ip: str
    dest_ip: str
    src_port: int
    dest_port: int
    protocol: int 
    src_ip, dest_ip, src_port, dest_port, protocol = flow
    src_ip = ip_to_integer(src_ip)
    dest_ip = ip_to_integer(dest_ip)
    HX = src_ip * 97 ^ dest_ip * 97 ^ src_port * 97 ^ dest_port * 97 ^ protocol * 97  
    return HX

def hashct1(flow: tuple[str, str, int, int, int], filter_size: int):
    src_ip: str
    dest_ip: str
    src_port: int
    dest_port: int
    protocol: int 
    src_ip, dest_ip, src_port, dest_port, protocol = flow
    src_ip = ip_to_integer(src_ip)
    dest_ip = ip_to_integer(dest_ip)
    HX = src_ip * 65 ^ dest_ip * 65 ^ src_port * 65 ^ dest_port * 65 ^ protocol * 65 
    return HX
