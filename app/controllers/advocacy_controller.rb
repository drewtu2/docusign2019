class AdvocacyController < ApplicationController
  def index
    if session[:supporting_issue].present?
      @thank = "true"
      @supporting_issue = session.delete(:supporting_issue)
      Advocacy.create(user_id: session[:user_id], issue_id: session[:issue_id])
      result = `python3 ./lib/scripts/get_reps.py --zip "50014"`
      # Get senator details
      @sent_to = "Senator #{result.split("\n").first.split(",")[-3].split("'").last} at #{result.split("\n").first.split(",").last.split("'")[1]}"
    end

    if params[:donation].present?
      @thank = "true"
      @donation = "true"
    end
    @issues = Issue.all
    @supported = User.find(session[:user_id]).advocacies.map(&:issue_id)
  end

  def edit
    # TODO : CALL script and get docusign redirect path. Check what to send.
    session[:issue_id] = params[:id]
    session[:supporting_issue] = Issue.find(params[:id]).title

    result = `python3 ./lib/scripts/ICareActivity.py --hostUrl="http://08eca4bc.ngrok.io"`
    url= result.split("\n")[-1]
    # Advocacy.create(user_id: session[:user_id], issue_id: params[:id])
    redirect_to url
  end
end
