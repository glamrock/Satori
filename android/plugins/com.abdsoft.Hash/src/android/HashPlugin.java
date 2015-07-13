/**
 * 
 * Phonegap Hash plugin
 * 
 * Version 1.0
 * 
 * Abdeslam Aabidi 2014
 * 
 * Email: xinony@gmail.com
 * 
 */
 
package com.abdsoft.Hash;

import org.apache.cordova.CordovaPlugin;
import org.apache.cordova.CallbackContext;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * This class Hash a string called from JavaScript.
 */
public class HashPlugin extends CordovaPlugin 
{
    @Override
    public boolean execute(String action, JSONArray args, CallbackContext callbackContext) throws JSONException 
    {
    	try
    	{
			JSONObject params = args.getJSONObject(0);
            String data = params.getString("data");
            String hash = params.getString("hash").toLowerCase(); // md5, sha1, sha-256, sha-384, sha-512
			
	        if (action.equals("hashString")) 
	        {
				callbackContext.success(hashString(data, hash));
	            return true;
	        }
	        else if (action.equals("hashFile"))
	        {
	        	callbackContext.success(hashFile(data, hash));
	        	return true;
	        }
    	}
    	catch (Exception e)
		{
			callbackContext.success(e.getMessage());
		}
    	
        return false;
    }

    public boolean isMDAvailable(String hash)
    {
        try
        {
        	MessageDigest.getInstance(hash);
        }
        catch(NoSuchAlgorithmException x)
        {
             return false;
        }
        return true;
    }
    
    private String hashString(String data, String hash) throws NoSuchAlgorithmException, IOException 
    {
    	if(isMDAvailable(hash) == false) 
    	{
    		return "Invalid Hash algorithm.";
    	}
    	
    	MessageDigest md = MessageDigest.getInstance(hash);
        md.reset();
        md.update(data.getBytes());
        
    	byte[] bytes = md.digest();
		BigInteger bi = new BigInteger(1, bytes);
		
		return bi.toString(16).toUpperCase();
    }
    
    private String hashFile(String data, String hash) throws NoSuchAlgorithmException, IOException 
    {   	
    	if(isMDAvailable(hash) == false) 
    	{
    		return "Invalid Hash algorithm.";
    	}
        
        File file = new File(data);
    	if (!file.exists())
    	{
    		return "File does not exist.";
    	}
        
    	MessageDigest md = MessageDigest.getInstance(hash);
        md.reset();
    	
    	InputStream is = new FileInputStream(file);
		byte[] buffer = new byte[8192];
		int read = 0;
		
		while((read = is.read(buffer)) > 0)
		{
			md.update(buffer, 0, read);
		}
		is.close();
    	
    	byte[] bytes = md.digest();
		BigInteger bi = new BigInteger(1, bytes);
		
		return bi.toString(16).toUpperCase();
    }    
}