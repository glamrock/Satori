package com.maginsoft.adapters;

import java.util.ArrayList;
import java.util.List;

import com.maginsoft.data.Category;

import android.app.Activity;
import android.content.Context;
import android.graphics.Typeface;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.ImageView;

public class DirectoryAdapter extends BaseAdapter {
    Context _context;
    ArrayList<Category> _categories;
	int _currentIndex;
	public DirectoryAdapter(Context context, ArrayList<Category> categories, int currentIndex)
	{
	    _context = context;
	    _categories = categories;
	    _currentIndex = currentIndex;
	}
	
	@Override
	public int getCount() {
		// TODO Auto-generated method stub
		return _categories.size();
	}

	@Override
	public Object getItem(int position) {
		// TODO Auto-generated method stub
		return _categories.get(position);
	}

	@Override
	public long getItemId(int position) {
		// TODO Auto-generated method stub
		return 0;
	}
	
	public void setCurrentIndex(int index)
	{
		_currentIndex = index;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		// TODO Auto-generated method stub
		
		int drawer = _context.getResources().getIdentifier("drawer_list_item", "layout", _context.getPackageName());
		View v;
		Activity act = (Activity) _context;
		
		LayoutInflater li = act.getLayoutInflater();
	
		v = li.inflate(drawer,parent,false);
		
		int menu = _context.getResources().getIdentifier("menuItem", "id", _context.getPackageName());
		android.widget.TextView tv = (android.widget.TextView)v.findViewById(menu);
		tv.setText(_categories.get(position).title);
		
		return v;
	}
     


}
