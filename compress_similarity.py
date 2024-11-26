import pickle
import gzip

with open('similarity.pkl', 'rb') as f_in:
    with gzip.open('similarity.pkl.gz', 'wb', compresslevel=9) as f_out:
        while True:
            chunk = f_in.read(1024 * 1024)  # Read in chunks
            if not chunk:
                break
            f_out.write(chunk)
