class CreateIssues < ActiveRecord::Migration[5.2]
  def change
    create_table :issues do |t|
      t.string :title
      t.string :attachment_link
      t.integer :supported
      t.text :description
      t.timestamps
    end
  end
end
