import DatabaseGateway

if __name__ == "__main__":
    parser=argparse.ArgumentParser()

    parser.add_argument('--userId', default="000", type=str, help='User id (000)')
    parser.add_argument('--issueId', default="issue1", type=str, help='IssueId ("issue1")')
    parser.add_argument('--hostUrl', default="localhost:5000", type=str, help='HostUrl ("localhost:5000")')
    args=parser.parse_args()

    activity = ICareActivity()
    return_url = activity.run(args.userId, args.issueId, args.hostUrl)
    
    print("Return Url: " + return_url)

