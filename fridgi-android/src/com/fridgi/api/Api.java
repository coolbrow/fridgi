package com.fridgi.api;

import com.fridgi.models.BaseIngredient;
import com.fridgi.models.Fridge;
import com.fridgi.models.Recipe;
import com.fridgi.util.Parsers;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class Api {
    private static final String BASE_URL = "http://fridgi.herokuapp.com";
    private static final String INGREDIENTS_URL = BASE_URL + "/ingredients";
    private static final String RECIPES_URL = BASE_URL + "/recipes";
    private static final String FRIDGE_URL = BASE_URL + "/fridge/";
    
    private static String getHttpResponse(String url) {
        URL serverAddress;
        try {
            serverAddress = new URL(url);
      
            HttpURLConnection connection = (HttpURLConnection)serverAddress.openConnection();
            connection.setRequestMethod("GET");
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder stringBuilder = new StringBuilder();

            String line = null;
            while ((line = reader.readLine()) != null)
            {
              stringBuilder.append(line + "\n");
            }
            reader.close();
            return stringBuilder.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    
    public static ArrayList<BaseIngredient> getIngredients(){
            try {
                JSONArray ingredientsJSON = new JSONArray(getHttpResponse(INGREDIENTS_URL));
                return Parsers.parseBaseIngredientArray(ingredientsJSON);
            } catch (JSONException e) {
                e.printStackTrace();
                return null;
            }
    }
    
    public static ArrayList<Recipe> getRecipes(){
        try {
            JSONArray recipesJSON = new JSONArray(getHttpResponse(RECIPES_URL));
            return Parsers.parseRecipeArray(recipesJSON);
        } catch (JSONException e) {
            e.printStackTrace();
            return null;
        }
    }
    
    public static Fridge getFridge(String name) {
        try {
            JSONObject fridgeJSON = new JSONObject(getHttpResponse(FRIDGE_URL + name));
            return Parsers.parseFridge(fridgeJSON);
        } catch (JSONException e) {
            e.printStackTrace();
            return null;
        }
    }
}