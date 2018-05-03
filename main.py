from blockchaincluster import BlockChainCluster
import pickle


def main():
    cluster = BlockChainCluster()
    for i in range(0, 10):
        cluster.add_blockchain_unit(str(i))
    cluster.retrieve_units()
    value = pickle.dumps(cluster)
    with open('chain.pkl', 'wb+') as p:
        p.write(value)
    input("You can make any changes to the pickle file to check robustness \
and press any key")
    try:
        with open('chain.pkl', 'rb') as c:
            newCluster = pickle.loads(c.read())
        newCluster.retrieve_units()
    except:
        print ("Structural Integrity of Blockchain compromised")


if __name__ == '__main__':
    main()
