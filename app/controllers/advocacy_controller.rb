class AdvocacyController < ApplicationController
  def index
    @thank = "true" if params[:thank].present?
    @issues = Issue.all
    @supported = User.find(session[:user_id]).advocacies.map(&:issue_id)
  end

  def edit
    # call and get redirect URL
    redirect_to advocacy_path
  end
end
