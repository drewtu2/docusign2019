class CreateAdvocacies < ActiveRecord::Migration[5.2]
  def change
    create_table :advocacies do |t|
      t.integer :user_id
      t.integer :issue_id
      t.timestamps
    end
  end
end
