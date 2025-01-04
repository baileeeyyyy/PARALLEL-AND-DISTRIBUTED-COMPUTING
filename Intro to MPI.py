
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

print("My rank is %i" % rank)

if rank == 1:
    data_send = "a"
    destination_process = 5
    source_process = 5

    comm.send(data_send, dest=destination_process)
    print("Sending data '%s' to process %d" % (data_send, destination_process))

    data_received = comm.recv(source=source_process)
    print("Data received is = '%s'" % data_received)

elif rank == 5:
    data_send = "b"
    destination_process = 1
    source_process = 1

    data_received = comm.recv(source=source_process)
    print("Data received is = '%s'" % data_received)

    comm.send(data_send, dest=destination_process)
    print("Sending data '%s' to process %d" % (data_send, destination_process))
