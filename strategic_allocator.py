import logging
from typing import Dict, Any
from allocation_models import ResourceAllocationModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class StrategicAllocator:
    """Allocates resources to maximize social impact and financial sustainability."""
    
    def __init__(self):
        self.allocation_model = ResourceAllocationModel()
        
    def allocate_resources(self, revenue_data: Dict[str, Any], 
                          impact_assessment: Dict[str, Any]) -> Dict[str, Any]:
        """Allocates resources based on revenue data and impact assessment."""
        try:
            # Calculate resource allocation
            allocation_strategy = self._determine_allocation_strategy(impact_assessment)
            logger.info(f"Selected allocation strategy: {allocation_strategy}")
            
            allocation_result = self.allocation_model.apply(allocation_strategy, 
                                                           revenue_data, 
                                                           impact_assessment)
            
            return allocation_result
            
        except Exception as e:
            logger