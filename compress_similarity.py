import pickle
import gzip

with open('similarity.pkl', 'rb') as f_in:
    with gzip.open('similarity.pkl.gz', 'wb') as f_out:
        # Read the file in chunks and write to the compressed file
        while True:
            chunk = f_in.read(1024 * 1024)  # Read 1MB at a time
            if not chunk:
                break
            f_out.write(chunk)
