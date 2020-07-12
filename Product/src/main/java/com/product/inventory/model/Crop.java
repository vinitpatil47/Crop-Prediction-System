package com.product.inventory.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="crop")
public class Crop {
	
	@Id
	@Column(name="index")
	private long index;
	
	@Column(name="state_name")
	private String state_name;
	
	@Column(name="district_name")
	private String district_name;
	
	@Column(name="crop_year")
	private int crop_year;
	
	@Column(name="season")
	private String season;
	
	@Column(name="crop")
	private String crop;
	
	@Column(name="area")
	private double area;
	
	@Column(name="production")
	private double production;
	
	@Column(name="rainfall")
	private double rainfall;

	public Crop() {
		super();
		// TODO Auto-generated constructor stub
	}

	public Crop(long index, String state_name, String district_name, int crop_year, String season, String crop,
			double area, double production, double rainfall) {
		super();
		this.index = index;
		this.state_name = state_name;
		this.district_name = district_name;
		this.crop_year = crop_year;
		this.season = season;
		this.crop = crop;
		this.area = area;
		this.production = production;
		this.rainfall = rainfall;
	}

	public long getIndex() {
		return index;
	}

	public void setIndex(long index) {
		this.index = index;
	}

	public String getState_name() {
		return state_name;
	}

	public void setState_name(String state_name) {
		this.state_name = state_name;
	}

	public String getDistrict_name() {
		return district_name;
	}

	public void setDistrict_name(String district_name) {
		this.district_name = district_name;
	}

	public int getCrop_year() {
		return crop_year;
	}

	public void setCrop_year(int crop_year) {
		this.crop_year = crop_year;
	}

	public String getSeason() {
		return season;
	}

	public void setSeason(String season) {
		this.season = season;
	}

	public String getCrop() {
		return crop;
	}

	public void setCrop(String crop) {
		this.crop = crop;
	}

	public double getArea() {
		return area;
	}

	public void setArea(double area) {
		this.area = area;
	}

	public double getProduction() {
		return production;
	}

	public void setProduction(double production) {
		this.production = production;
	}

	public double getRainfall() {
		return rainfall;
	}

	public void setRainfall(double rainfall) {
		this.rainfall = rainfall;
	}

	@Override
	public String toString() {
		return "Crop [index=" + index + ", state_name=" + state_name + ", district_name=" + district_name
				+ ", crop_year=" + crop_year + ", season=" + season + ", crop=" + crop + ", area=" + area
				+ ", production=" + production + ", rainfall=" + rainfall + "]";
	}	

}
