class AddSummaryToIssues < ActiveRecord::Migration[5.2]
  def change
    add_column :issues, :summary, :text
  end
end
