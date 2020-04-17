# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == 1:
	data = "Pesan"
	for i in range (0,size):
                comm.send(data, dest=i, tag=i)
                print("rank :", rank, "dengan data :", data, "destination :",i)

# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
	data = comm.recv(source = size-1)
	print("rank :", rank, "dengan data :", data)
