package com.orleonsoft.android.simplefilechooser.ui;

import java.io.File;
import java.io.FileFilter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import com.maginsoft.adapters.DirectoryAdapter;
import com.maginsoft.data.Category;
import com.maginsoft.utils.Utils;
import com.orleonsoft.android.simplefilechooser.Constants;
import com.orleonsoft.android.simplefilechooser.FileInfo;
import com.orleonsoft.android.simplefilechooser.adapters.FileArrayAdapter;

import android.app.Activity;
import android.app.ListActivity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Environment;
import android.support.v4.app.ActionBarDrawerToggle;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.util.Log;
import android.view.KeyEvent;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.ListView;

public class FileChooserActivity extends ListActivity implements OnItemClickListener {

	private File currentFolder;
	private FileArrayAdapter fileArrayListAdapter;
	private FileFilter fileFilter;
	private File fileSelected;
	private ArrayList<String> extensions;
	private DrawerLayout mDrawerLayout;
	private ListView mDrawerList;
	private ActionBarDrawerToggle mDrawerToggle;
	int currentIndex;
	ArrayList<Category> _category;
	Context _context;
	Category currentCategory;
	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		int main = this.getResources().getIdentifier("main", "layout", this.getPackageName());
		int internal = this.getResources().getIdentifier("internal", "string", this.getPackageName());
		
		int drawer_layout = this.getResources().getIdentifier("drawer_layout", "id", this.getPackageName());
		int left_drawer = this.getResources().getIdentifier("left_drawer", "id", this.getPackageName());
		int drawer_shadow = this.getResources().getIdentifier("drawer_shadow", "drawable", this.getPackageName());
		int ic_navigation_drawer = this.getResources().getIdentifier("ic_navigation_drawer", "drawable", this.getPackageName());

		int drawer_open = this.getResources().getIdentifier("drawer_open", "string", this.getPackageName());
		int drawer_close = this.getResources().getIdentifier("drawer_close", "string", this.getPackageName());

		setContentView(main);

	    getActionBar().setDisplayHomeAsUpEnabled(true);
	    getActionBar().setHomeButtonEnabled(true);
		_context = this;
		Bundle extras = getIntent().getExtras();
		if (extras != null) {
			if (extras
					.getStringArrayList(Constants.KEY_FILTER_FILES_EXTENSIONS) != null) {
				extensions = extras
						.getStringArrayList(Constants.KEY_FILTER_FILES_EXTENSIONS);
				fileFilter = new FileFilter() {
					@Override
					public boolean accept(File pathname) {
						return ((pathname.isDirectory()) || (pathname.getName()
								.contains(".") ? extensions.contains(pathname
								.getName().substring(
										pathname.getName().lastIndexOf(".")).toLowerCase())
								: false));
					}
				};
			}
		}
		currentFolder = new File(Environment.getExternalStorageDirectory()
				.getAbsolutePath());
		
		currentCategory = new Category();
		currentCategory.title = getString(internal);
		currentCategory.path = currentFolder.getAbsolutePath(); 
				
	    mDrawerLayout = (DrawerLayout) findViewById(drawer_layout);
	    mDrawerLayout.setDrawerShadow(drawer_shadow,GravityCompat.START);
 		mDrawerList = (ListView) findViewById(left_drawer);
	    mDrawerToggle = new ActionBarDrawerToggle(this, /* host Activity */
	    	 mDrawerLayout, /* DrawerLayout object */
	    	 ic_navigation_drawer, /* nav drawer image to replace 'Up' caret */
	    	 drawer_open, /* "open drawer" description for accessibility */
	    	 drawer_close /* "close drawer" description for accessibility */
	    	 ) {
	    	     public void onDrawerClosed(View view) 
	    	     {
	    	           // getSupportActionBar().setTitle(mTitle);
	    	            invalidateOptionsMenu(); // creates call to
	    	                                            // onPrepareOptionsMenu()
	    	     }

	    	     public void onDrawerOpened(View drawerView) 
	    	     {
	    	           // getSupportActionBar().setTitle(mDrawerTitle);
	    	            invalidateOptionsMenu(); // creates call to
	    	                                            // onPrepareOptionsMenu()
	    	     }
	           };
	           
	   mDrawerLayout.post(new Runnable() {
	               @Override
	               public void run() {
	                   mDrawerToggle.syncState();
	               }
	           });
	    	     
	    mDrawerLayout.setDrawerListener(mDrawerToggle);
	  //  ActionBar.
	    //getSupportActionBar().set

		fill(currentFolder);
	}
	  
	
    @Override
	public boolean onOptionsItemSelected(MenuItem item)
	{
		switch (item.getItemId()) {
	      case android.R.id.home:	    		
	    	  if (mDrawerLayout.isDrawerOpen(mDrawerList)){
	    		    mDrawerLayout.closeDrawer(mDrawerList);
	    		} else {
	    			_category = new ArrayList<Category>();
	    			//File file = Environment.getExternalStorageDirectory();
	    			/*Category cat0 = new Category();
	    			cat0.path = file.getAbsolutePath();
	    			cat0.title = "Internal";
	    			*/
	    			_category.add(Utils.getInternalStorage(this));
	    			
	    			Category catExt = Utils.getExternalStorage(this);
	    			if(catExt!=null)
	    			{
	    				_category.add(catExt);
	    			}
	    			
	    		    mDrawerList.setAdapter(new DirectoryAdapter(_context, _category,currentIndex));
	    		    mDrawerList.setOnItemClickListener(new AdapterView.OnItemClickListener()
	    		    {
	    		    	@Override
	    		    	public void onItemClick(AdapterView<?> arg0, View arg1,
	    		    			int arg2, long arg3) {
	    		    		 currentIndex = arg2;
	    		    		 DirectoryAdapter adapter = (DirectoryAdapter) mDrawerList.getAdapter();
	    		    		 adapter.setCurrentIndex(arg2);
	    		    		 Category cat = (Category) arg0.getItemAtPosition(arg2);
	    		    		 currentCategory = cat;
	    		    		 fill(new File(cat.path));
	    		    	   
	    		    	     mDrawerLayout.closeDrawer(mDrawerList);
	    		    	     adapter.notifyDataSetChanged();
	    		    	}
	    		    });
	    		   

	    		    mDrawerLayout.openDrawer(mDrawerList);
	    		}
			  return true;
		  default:
			  return true;
		}	
	}

	/*public boolean onKeyDown(int keyCode, KeyEvent event) {
		if (keyCode == KeyEvent.KEYCODE_BACK) {
			/*if ((!currentFolder.getName().equals(
					Environment.getExternalStorageDirectory().getName()))
					&& (currentFolder.getParentFile() != null)) {
				currentFolder = currentFolder.getParentFile();
				fill(currentFolder);
			} else {
				Log.i("FILE CHOOSER", "canceled");
				setResult(Activity.RESULT_CANCELED);				
				finish();
			}
			return true;
		}
		return super.onKeyDown(keyCode, event);
	}
*/
   
    
	private void fill(File f) {
		File[] folders = null;
		if (fileFilter != null)
			folders = f.listFiles(fileFilter);
		else
			folders = f.listFiles();

		if(f.getAbsolutePath().trim().equalsIgnoreCase(currentCategory.path.trim()) == true)
		{
			this.setTitle(currentCategory.title + ": /");
		}
		else
		{
		    this.setTitle(currentCategory.title + ": " + f.getName());
		}
		
		int fileSize = this.getResources().getIdentifier("fileSize", "string", _context.getPackageName());
		List<FileInfo> dirs = new ArrayList<FileInfo>();
		List<FileInfo> files = new ArrayList<FileInfo>();
		try {
			for (File file : folders) {
				if (file.isDirectory() && !file.isHidden())
					//si es un directorio en el data se ponemos la contante folder
					dirs.add(new FileInfo(file.getName(),
							Constants.FOLDER, file.getAbsolutePath(),
							true, false));
				else {
					if (!file.isHidden())
						files.add(new FileInfo(file.getName(),
								getString(fileSize) + ": "
										+ file.length(),
								file.getAbsolutePath(), false, false));
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		Collections.sort(dirs);
		Collections.sort(files);
		dirs.addAll(files);
		
		/*if (!f.getName().equalsIgnoreCase(
				Environment.getExternalStorageDirectory().getName())) {
			if (f.getParentFile() != null)
			//si es un directorio padre en el data se ponemos la contante adeacuada
				dirs.add(0, new FileInfo("..",
						Constants.PARENT_FOLDER, f.getParent(),
						false, true));
		}*/
		
		if (!f.getAbsolutePath().equalsIgnoreCase(
				currentCategory.path)) {
			if (f.getParentFile() != null)
			//si es un directorio padre en el data se ponemos la contante adeacuada
				dirs.add(0, new FileInfo("..",
						Constants.PARENT_FOLDER, f.getParent(),
						false, true));
		}
		
		int file_row = this.getResources().getIdentifier("file_row", "layout", _context.getPackageName());
		
		fileArrayListAdapter = new FileArrayAdapter(FileChooserActivity.this,
				file_row, dirs);
		
		//ListView lv = (ListView)findViewById(R.id.list);
		//lv.setOnItemClickListener(this);
		//lv.setAdapter(fileArrayListAdapter);
		
		this.setListAdapter(fileArrayListAdapter);
	}

	@Override
	protected void onListItemClick(ListView l, View v, int position, long id) {

		super.onListItemClick(l, v, position, id);
		FileInfo fileDescriptor = fileArrayListAdapter.getItem(position);
		if (fileDescriptor.isFolder() || fileDescriptor.isParent()) {
			currentFolder = new File(fileDescriptor.getPath());
			fill(currentFolder);
		} else {

			fileSelected = new File(fileDescriptor.getPath());
			Intent intent = new Intent();
			intent.putExtra(Constants.KEY_FILE_SELECTED,
					fileSelected.getAbsolutePath());
			setResult(Activity.RESULT_OK, intent);
			Log.i("FILE CHOOSER", "result ok");
			finish();
		}
	}

	@Override
	public void onItemClick(AdapterView<?> parent, View view, int position,
			long id) {
		// TODO Auto-generated method stub
		//super.onListItemClick(l, v, position, id);
		FileInfo fileDescriptor = fileArrayListAdapter.getItem(position);
		if (fileDescriptor.isFolder() || fileDescriptor.isParent()) {
			currentFolder = new File(fileDescriptor.getPath());
			fill(currentFolder);
		} else {

			fileSelected = new File(fileDescriptor.getPath());
			Intent intent = new Intent();
			intent.putExtra(Constants.KEY_FILE_SELECTED,
					fileSelected.getAbsolutePath());
			setResult(Activity.RESULT_OK, intent);
			Log.i("FILE CHOOSER", "result ok");
			finish();
		}
	}
	
	@Override
	public void onBackPressed() {
	   Log.d("CDA", "onBackPressed Called");
		setResult(Activity.RESULT_CANCELED, null);
		Log.i("FILE CHOOSER", "result ok");
		finish();
	}

}