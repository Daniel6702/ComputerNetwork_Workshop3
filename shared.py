import time
import struct

'''32-bit pre-shared key'''
KEY = b'abcd'  #b for byte string (4 bytes = 32 bits)

def xor_encrypt_decrypt(data, key):
    '''Performs XOR encryption/decryption on the given data using the provided key.'''
    result = []

    for i in range(4): # 4 bytes = 32 bits
        # Perform XOR operation between the corresponding elements of data and key
        xor_result = data[i] ^ key[i]
        result.append(xor_result)

    # Convert the result list back into bytes and return it
    return bytes(result)

def get_RFC_868_timestamp():
    '''Returns the current time in seconds since midnight, January 1, 1900 (RFC 868).'''
    return int(time.time()) + 2208988800

def convert_RFC_868_timestamp_to_time(timestamp):
    '''Converts the given RFC 868 timestamp to a human-readable time string.'''
    return time.ctime(timestamp)

def get_encrypted_timestamp(key):
    '''Encrypts the current RFC 868 timestamp using the given key.'''
    timestamp = get_RFC_868_timestamp()
    timestamp_bytes = struct.pack('!I', timestamp)
    encrypted_timestamp = xor_encrypt_decrypt(timestamp_bytes, key)
    return encrypted_timestamp

def calculate_clock_skew(server_time, client_time):
    '''Calculates the clock skew between the server and client.'''
    return server_time - client_time

def analyze_received_timestamp(data, key):
    '''Decrypts the received timestamp and calculates the clock skew.'''
    decrypted_timestamp = xor_encrypt_decrypt(data, key)
    server_time = struct.unpack('!I', decrypted_timestamp)[0] - 2208988800
    client_time = int(time.time())
    clock_skew = calculate_clock_skew(server_time, client_time)
    return clock_skew, convert_RFC_868_timestamp_to_time(server_time), convert_RFC_868_timestamp_to_time(client_time)