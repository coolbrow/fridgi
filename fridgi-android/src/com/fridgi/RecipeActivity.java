package com.fridgi;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.DialogInterface.OnClickListener;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;
import android.widget.TextView;

import com.commonsware.cwac.merge.MergeAdapter;
import com.fridgi.adapters.RecipeIngredientAdapter;
import com.fridgi.models.Recipe;
import com.fridgi.models.RecipeIngredient;
import com.fridgi.tasks.AddToGroceryTask;
import com.fridgi.util.Globals;

public class RecipeActivity extends FragmentActivity {
    
    public static String INTENT_EXTRA_RECIPE = "INTENT_EXTRA_RECIPE";
    
    private MergeAdapter mAdapter;
    private RecipeIngredient mSelected;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.recipe);
        
        Recipe recipe = getIntent().getParcelableExtra(INTENT_EXTRA_RECIPE);
        
        mAdapter = new MergeAdapter();
        
        LayoutInflater inflater = getLayoutInflater();
        TextView title = (TextView) inflater.inflate(R.layout.title, null);
        title.setText(recipe.getName());
        
        mAdapter.addView(title);
        
        RecipeIngredientAdapter ingredients = new RecipeIngredientAdapter(this, recipe.getIngredients());
        mAdapter.addAdapter(ingredients);
        
        StringBuilder sb = new StringBuilder();
        String[] instructions = recipe.getInstructions();
        for (int i = 0; i < instructions.length; i++) {
            sb.append(instructions[i] + "\n\n");
        }
        TextView instructionsView = (TextView) inflater.inflate(R.layout.text, null);
        instructionsView.setText(sb.toString());
        mAdapter.addView(instructionsView);
        
        ListView list = (ListView) findViewById(R.id.list);
        list.setOnItemClickListener(mOnIngredientClickedListener);
        list.setAdapter(mAdapter);
    }
    
    OnItemClickListener mOnIngredientClickedListener = new OnItemClickListener() {

        @Override
        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
            Object obj = mAdapter.getItem(position);
            if (obj instanceof RecipeIngredient) {
                mSelected = (RecipeIngredient) obj;
                AlertDialog dialog = new AlertDialog.Builder(RecipeActivity.this)
                    .setMessage("Are you sure you want to add " + mSelected.getName() + " to your list?")
                    .setPositiveButton("OK", mOnAddListener)
                    .create();
                dialog.show();
            }
        }
    };
    
    OnClickListener mOnAddListener = new OnClickListener() {
        
        @Override
        public void onClick(DialogInterface dialog, int which) {
            AddToGroceryTask task = new AddToGroceryTask(Globals.getInstance().getFridge().getName(), 
                    mSelected.getIngredient().getId(), 
                    mSelected.getQuantity());
            task.execute();
        }
    };

}
