package com.product.inventory.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.product.inventory.repository.croprepo;

@CrossOrigin(origins = "http://localhost:4200")
@RestController
public class CropController {
	
	@Autowired
	croprepo repo;
	
	@GetMapping("/getstate")
	public List<String> getstate()
	{
		return repo.getstate();
	}
	
	@GetMapping("/getdistrict/{state_name}")
	public List<String> getdistrict(@PathVariable String state_name)
	{
		return repo.getdistrict(state_name);
	}
	
	@GetMapping("/getcrop/{state_name}/{district_name}")
	public List<String> getcrop(@PathVariable String state_name,@PathVariable String district_name)
	{
		return repo.getcrop(state_name,district_name);
	}

}
