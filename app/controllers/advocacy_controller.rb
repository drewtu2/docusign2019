class AdvocacyController < ApplicationController
  def index
    if session[:supporting_issue].present?
      @thank = "true"
      @supporting_issue = session.delete(:supporting_issue)
      # Get senator details
      @sent_to = "Senator BLA BLA BLA at blabla@blabl.com"
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
    session[:supporting_issue] = Issue.find(params[:id]).title
    # Advocacy.create(user_id: session[:user_id], issue_id: params[:id])
    redirect_to advocacy_path
  end
end
