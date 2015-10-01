package com.orleonsoft.android.simplefilechooser.adapters;

import java.util.List;

import android.annotation.SuppressLint;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.orleonsoft.android.simplefilechooser.Constants;
import com.orleonsoft.android.simplefilechooser.FileInfo;

@SuppressLint("DefaultLocale")
public class FileArrayAdapter extends ArrayAdapter<FileInfo> {

	private Context context;
	private int resorceID;
	private List<FileInfo> items;

	public FileArrayAdapter(Context context, int textViewResourceId,
			List<FileInfo> objects) {
		super(context, textViewResourceId, objects);
		this.context = context;
		this.resorceID = textViewResourceId;
		this.items = objects;
	}

	public FileInfo getItem(int i) {
		return items.get(i);
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		ViewHolder viewHolder;
		
		int name1 = context.getResources().getIdentifier("name", "id", context.getPackageName());
		int detail = context.getResources().getIdentifier("details", "id", context.getPackageName());
		if (convertView == null) {
			LayoutInflater layoutInflater = (LayoutInflater) context
					.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
			convertView = layoutInflater.inflate(resorceID, null);
			viewHolder = new ViewHolder();
			viewHolder.icon = (ImageView) convertView
					.findViewById(android.R.id.icon);
			viewHolder.name = (TextView) convertView.findViewById(name1);
			viewHolder.details = (TextView) convertView
					.findViewById(detail);
			convertView.setTag(viewHolder);
		} else {
			viewHolder = (ViewHolder) convertView.getTag();
		}

		FileInfo option = items.get(position);
		if (option != null) {
			int folder = context.getResources().getIdentifier("folder", "drawable", context.getPackageName());
			int xls = context.getResources().getIdentifier("xls", "drawable", context.getPackageName());
			int doc = context.getResources().getIdentifier("doc", "drawable", context.getPackageName());
			int back = context.getResources().getIdentifier("back", "drawable", context.getPackageName());
			
			int ppt = context.getResources().getIdentifier("ppt", "drawable", context.getPackageName());
			int pdf = context.getResources().getIdentifier("pdf", "drawable", context.getPackageName());
			int apk = context.getResources().getIdentifier("apk", "drawable", context.getPackageName());
			int txt = context.getResources().getIdentifier("txt", "drawable", context.getPackageName());

			int jpg = context.getResources().getIdentifier("jpg", "drawable", context.getPackageName());
			int png = context.getResources().getIdentifier("png", "drawable", context.getPackageName());

			int zip = context.getResources().getIdentifier("zip", "drawable", context.getPackageName());
			int rtf = context.getResources().getIdentifier("rtf", "drawable", context.getPackageName());

			int gif = context.getResources().getIdentifier("gif", "drawable", context.getPackageName());
			int avi = context.getResources().getIdentifier("avi", "drawable", context.getPackageName());

			int mp3 = context.getResources().getIdentifier("mp3", "drawable", context.getPackageName());
			int mp4 = context.getResources().getIdentifier("mp4", "drawable", context.getPackageName());
			
			int rar = context.getResources().getIdentifier("rar", "drawable", context.getPackageName());
			int aac = context.getResources().getIdentifier("aac", "drawable", context.getPackageName());
			
			int odt = context.getResources().getIdentifier("odt", "drawable", context.getPackageName());
			int ods = context.getResources().getIdentifier("ods", "drawable", context.getPackageName());
			
			int odp = context.getResources().getIdentifier("odp", "drawable", context.getPackageName());
			int blank = context.getResources().getIdentifier("blank", "drawable", context.getPackageName());

			if (option.getData().equalsIgnoreCase(Constants.FOLDER)) {
				viewHolder.icon.setImageResource(folder);
			} else if (option.getData().equalsIgnoreCase(
					Constants.PARENT_FOLDER)) {
				
				viewHolder.icon.setImageResource(back);
			} else {
				String name = option.getName().toLowerCase();
				if (name.endsWith(Constants.XLS)
						|| name.endsWith(Constants.XLSX))
					viewHolder.icon.setImageResource(xls);
				else if (name.endsWith(Constants.DOC)
						|| name.endsWith(Constants.DOCX))
					viewHolder.icon.setImageResource(doc);
				else if (name.endsWith(Constants.PPT)
						|| option.getName().endsWith(Constants.PPTX))
					viewHolder.icon.setImageResource(ppt);
				else if (name.endsWith(Constants.PDF))
					viewHolder.icon.setImageResource(pdf);
				else if (name.endsWith(Constants.APK))
					viewHolder.icon.setImageResource(apk);
				else if (name.endsWith(Constants.TXT))
					viewHolder.icon.setImageResource(txt);
				else if (name.endsWith(Constants.JPG)
						|| name.endsWith(Constants.JPEG))
					viewHolder.icon.setImageResource(jpg);
				else if (name.endsWith(Constants.PNG))
					viewHolder.icon.setImageResource(png);
				else if (name.endsWith(Constants.ZIP))
					viewHolder.icon.setImageResource(zip);
				else if (name.endsWith(Constants.RTF))
					viewHolder.icon.setImageResource(rtf);
				else if (name.endsWith(Constants.GIF))
					viewHolder.icon.setImageResource(gif);
				else if (name.endsWith(Constants.AVI))
					viewHolder.icon.setImageResource(avi);
				else if (name.endsWith(Constants.MP3))
					viewHolder.icon.setImageResource(mp3);
				else if (name.endsWith(Constants.MP4))
					viewHolder.icon.setImageResource(mp4);
				else if (name.endsWith(Constants.RAR))
					viewHolder.icon.setImageResource(rar);
				else if (name.endsWith(Constants.ACC))
					viewHolder.icon.setImageResource(aac);
				else if (name.endsWith(Constants.ODT))
					viewHolder.icon.setImageResource(odt);
				else if (name.endsWith(Constants.ODS))
					viewHolder.icon.setImageResource(ods);
				else if (name.endsWith(Constants.ODP))
					viewHolder.icon.setImageResource(odp);
				else
					viewHolder.icon.setImageResource(blank);
			}

			viewHolder.name.setText(option.getName());
			viewHolder.details.setText(option.getData());

		}
		return convertView;
	}

	class ViewHolder {
		ImageView icon;
		TextView name;
		TextView details;
	}

}
