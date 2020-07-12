package com.product.inventory.repository;

import java.util.List;

import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import com.product.inventory.model.Crop;

public interface croprepo extends CrudRepository<Crop,Long> {

	@Query("SELECT DISTINCT state_name FROM Crop order by state_name")
	public List<String> getstate();
	
	@Query("SELECT DISTINCT district_name FROM Crop WHERE state_name=?1 order by district_name")
	public List<String> getdistrict(String state_name);
	
	@Query("SELECT DISTINCT crop FROM Crop WHERE state_name=?1 and district_name=?2 order by crop")
	public List<String> getcrop(String state_name,String district_name);
}
